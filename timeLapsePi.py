from picamera import PiCamera
import errno
import os
import sys
from threading import Timer
from datetime import datetime
from time import sleep 
import yaml

config = yaml.safe_load(open(os.path.join(sys.path[0], "timeLapseConfig.yml")))

def create_timestamped_dir(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def set_camera_options(camera):
    # Set camera resolution.
    if config['resolution']:
        camera.resolution = (
            config['resolution']['width'],
            config['resolution']['height']
        )

    # Set ISO.
    if config['iso']:
        camera.iso = config['iso']

    # Set shutter speed.
    if config['shutter_speed']:
        camera.shutter_speed = config['shutter_speed']
        # Sleep to allow the shutter speed to take effect correctly.
        sleep(1)
        camera.exposure_mode = 'off'

    # Set white balance.
    if config['white_balance']:
        camera.awb_mode = 'off'
        camera.awb_gains = (
            config['white_balance']['red_gain'],
            config['white_balance']['blue_gain']
        )

    # Set camera rotation
    if config['rotation']:
        camera.rotation = config['rotation']

    return camera

# Create directory based on current timestamp.
dir = os.path.join(
    sys.path[0],
    'series-' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
)
vfile = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
create_timestamped_dir(dir)

def takePic(x):
	   # Capture a picture.
           captureName = dir + '/image{0:05d}.jpg'.format(x)
           print '\ncaptureName='+captureName+'\n'
           camera.capture(captureName)
           #camera.close()

def createOutput():
	# TODO: These may not get called after the end of the threading process...
        # Create an animated gif (Requires ImageMagick).
        if config['create_gif']:
            print '\nCreating animated gif.\n'
            os.system('convert -delay 10 -loop 0 ' + dir + '/image*.jpg ' + dir + '-timelapse.gif')  # noqa

        # Create a video (Requires avconv - which is basically ffmpeg).
        if config['create_video']:
            print '\nCreating video.\n'
            os.system('sudo avconv -r 10 -i '+dir+'/image%05d.jpg -b:v 1000k -pix_fmt yuv420p '+dir+'/timelapse.mp4')  # noqa
	    #sudo avconv -r 10 -i /home/pi/Pictures/piCam/series-2018-12-01_14-55-08/image%05d.jpg -b:v 1000k 
	    #-pix_fmt yuv420p /home/pi/Pictures/piCam/series-2018-12-01_14-55-08/timelapse.mp4

def main():
	# Kick off the capture process.
	global camera
	camera = PiCamera()
        set_camera_options(camera)

	y = config['total_images']
        pause = config['interval']
	print "starting Loop...pause="+str(pause)+" totalImgs="+str(y)
	for w in range(y):
	   print "processing "+str(w)
	   try:
	      t = Timer(1, takePic, args=(w,))
	      t.start()
	   finally:
	      sleep(pause)
	      print '\nDone...'+str(w)+'\n'

main()
createOutput()
os.system('sudo cp '+dir+'/timelapse.mp4 /var/www/html/test/timeLapse'+vfile+'.mp4')
