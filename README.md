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
This project includes 2 files that allows the timeLapse functionality; timeLapsePi.py and timeLapseConfig.py. 
<b>timeLapseConfig.yml</b>: set the total_images variable to a large number—as large as you want, within Python's limitations. This way you won't start a timelapse and it stops after very few images are taken. Note: You can run the timeLapsePi.py via the Python script directly.
<p>
<h2>To Do (Future)</h2> -- Create a service on the system (e.g. start with systemctl start timelapse, stop with systemctl stop timelapse).
Copy the timelapse.service file into the Systemd unit file location: sudo cp timelapse.service /etc/systemd/system/timelapse.service.
Reload the Systemd daemon (sudo systemctl daemon-reload) to load in the new unit file.
Choose how you want to manage the timelapse service: To start a timelapse at system boot: sudo systemctl enable timelapse (disable to turn off, is-enabled to check current status) To start a timelapse at any time: sudo systemctl start timelapse (if one is not already running) To stop a timelapse in progress: sudo systemctl stop timelapse
