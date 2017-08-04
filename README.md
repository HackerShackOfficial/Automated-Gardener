# Automated-Gardener
Simple scheduler for a Raspberry Pi powered indoor gardener

## Running the Program

### Download the Code
Download the repository with Git `git clone https://github.com/HackerHouseYT/Automated-Gardener.git` 

or download the zip `wget https://github.com/HackerHouseYT/Automated-Gardener/archive/master.zip`

If you downloaded via zip, make sure to unzip the folder `unzip master.zip`

Navigate to into the folder

```
cd Automated-Gardener-master
```

### Modify the Gardener Program 

Open the file with `Vim` (if you don't have Vim installed, you can install it with `apt-get install vim`)

```
vim gardener.py
```

Press 'i' to edit

Modify the pin variables if your signal wires are connected to different pins on your Raspberry Pi.

```
LIGHT_PIN = 20
PUMP_PIN = 12
```

If you scroll down to the bottom, you can see where the schedule is set:

```
# Turn water on every 30 minutes for 10 seconds
schedule.every(30).minutes.do(threaded, water, forLength=10)

# Other scheduling examples
#schedule.every().hour.do(threaded, light, forLength=300)
#schedule.every().day.at("10:30").do(threaded, light, action=GardenerAction.turnOn)
#schedule.every().day.at("12:30").do(threaded, light, action=GardenerAction.turnOff)
#schedule.every().monday.do(threaded, water, forLength=30)
#schedule.every().wednesday.at("13:15").do(threaded, light, forLength=30)
```

`schedule.every(30).minutes.do(threaded, water, forLength=10)` turns the pump on for 10 seconds every 30 minutes. To change the schedule, you can uncomment some of the scheduling examples by removing the `#` at the start of the line and changing the time/day. For example, if I wanted to turn the light on for 30 minutes on Wednesday at 2:00 pm, I would write:

```
schedule.every().wednesday.at("14:00").do(threaded, light, forLength=1800)
```

After you've modified the gardener file, press `esc` to exit edit mode, then `:wq` to save and quit. 

### Install Dependencies
Install a couple dependencies before you start the program.

```
sudo pip install schedule
```

```
sudo pip install rpi.gpio
```

Run the program

```
python gardener.py
```

Press `control-c` to quit

### Running on Startup

Get the current working directory by running

```
pwd
```

Copy the path, then open `rc.local`

```
sudo vim /etc/rc.local
```

Press `i`. Before `exit 0`, add 

```
python <pwd output>/gardener.py
```

Press `esc` then `:wq!` to save and quit.

When you reboot the PI, the program should start!


