<h2>Usage</h2>
Raspberry Pi Zero W as a headless time-lapse camera.
Install dependencies: sudo apt-get install -y python-picamera python-yaml
Download or clone this repository to your Pi.
Copy timeLapseConfig.yml to config.yml.
Configure the time lapse setting by modifying values in config.yml.
In the Terminal, cd into this project directory and run python timeLapsePi.py.
After the capture is completed, the images will be stored in a directory named series-[current date].
<p>
<h2>Run on Raspberry Pi Startup and manage timelapses via Systemd</h2>
This project includes a Systemd unit file that allows the timelapse script to be managed like any other service on the system (e.g. start with systemctl start timelapse, stop with systemctl stop timelapse).

To use this feature, do the following:

In your config.yml, set the total_images variable to a large number—as large as you want, within Python's limitations. This way you won't start a timelapse and it stops after very few images are taken.
Copy the timelapse.service file into the Systemd unit file location: sudo cp timelapse.service /etc/systemd/system/timelapse.service.
Reload the Systemd daemon (sudo systemctl daemon-reload) to load in the new unit file.
Choose how you want to manage the timelapse service: 1. To start a timelapse at system boot: sudo systemctl enable timelapse (disable to turn off, is-enabled to check current status) 1. To start a timelapse at any time: sudo systemctl start timelapse (if one is not already running) 1. To stop a timelapse in progress: sudo systemctl stop timelapse
Note: You should not try running a timelapse via the Python script directly and via Systemd at the same time. This could do weird things, and is not a typical mode of operation!
