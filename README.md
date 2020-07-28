# Spoiled Pet App

## Robotic Treat Dispenser for the Spoiled Cat or Dog

### Description
The Spoiled Pet App 😸 is a robotic treat dispenser which can release treats to your spoiled pet via a text message you can send from anywhere in the US and Canada. A Picamera snaps a pic of your pet chowing away and sends it to your phone as an MMS.  

**Hardware**:
Raspberry pi with power supply, servo motor and cereal dispenser. The servo motor control horn is screwed to the handle of the dispenser and supported with 3m adhesive tape and an L bracket. I used a 30 degree rotation.

**Software**: I used *Twilio* for the text message account, *Flask* for the app and *Ngrok* to host my local server on a temporary https address. Twilio relays incoming sms messages to the Flask app through a webhook. I used a Python *subprocess* to call the motor rotation code which I also wrote in Python. Texts can be sent to the Twilio number to activate the dispenser from anywhere in the USA/Canada. I used *Cloudinary* to upload the images for sending.

**Automatic Treat Dispenser for Cat/Dog**:

1. Minimum Viable Product (MVP) – Automatically rotate the handle of a standard food dispenser using a motor via a text message or email. **complete**
2. Rotation will be triggered by a network interaction such as a tweet, an email or a text message to a certain account/address. **complete**
3. Picamera to photograph pet eating treats and save image. **complete**
4. User can respond ‘yes’ to trigger the mechanism which rotates and releases the treats or ‘no’ to have no action or just text ‘Treats’ to the number to activate the motor code. **complete**
5. Nice to Have: Save and send image of pet to user. **complete**

**Parts Needed/Used**:

* Servo or Stepper motor. Looking at a **FS5106R Continuous Rotation 360 degree Servo**.  If this does not work will try the **Feetech FS90R 360 Degree Continuous Rotation Micro Servo Motor**.  Will need to screw the rotator into the plastic handle of the cereal dispenser.  Cost $14.
* PiCamera - $12 on Amazon - **Arducam Octoprint Octopi Webcam, Monitor 3D Printer, 3.28FT/100CM Long Extension Flex Ribbon Cable**
* Small Cereal Dispenser - Looking at **Zevro KCH-06134 Compact Dry Food Dispenser, Dual Control, Black/Chrome for $26**
* Raspberry Pi with SD card, case and full kit. Looking at **CanaKit Raspberry Pi 3 Ultimate Starter Kit - 32 GB Edition**
* Screwdriver and drill.
* Battery pack or Power Supply – **LAMPVPATH (Pack of 2) 4 AA Battery Holder with Switch**, **6V Battery Holder with Switch or 5V 2.5A Power Supply** - $10-$12   
* Holder for the motor – cost undetermined at this time. Possibilities – **3 inch L Bracket** and **3m adhesive tape**, or **U column** with bolt and screw. $15-$20
* Ramp to slide treats off of the tray so cat can eat them - I made this from paper and then cardboard.

**Physical Constraints to work out from a Design Perspective:**

* How to attach rotator to the handle and have it rotate with the servo?  *See diagram*
* How much rotation to release the right amount of treats? *30 degree angle at 1.5 initiation*
* How to lock the dispenser to the counter or wall?  *duct tape and desk clamp*
* How to lock the motor to the dispenser so that the rotator piece turns and the motor does not?  *L bracket and adhesive tape or U column and bolt - used the former*
* Time – how long to run the entire process? .*Must be less than a ten seconds fully - actual time 9 seconds including image upload and send*
* How to allow for a reply from the user to call the rotation function code and rotate the motor remotely through the network? *SSH to trigger code from either an app or SMS or 'Call' function in Subprocess - used the later*
* Can pet access treats safety after treats are dispensed? *Added ramp to slide treats out*
* How to upload and send the pics from the picamera? *used Cloudinary api*. 

**Not part of MVP but nice to have**

* How to set up the pi camera - *done and saves a photo of pet eating when code executed*
* How to allow camera to capture the pet for more than 10 seconds? *decided to skip the motion detection piece and let the user activate the app when the user wants*
* How to send the picture with the text requesting the treat?  *Cloudinary and Twilio MMS with a config.ini file to store the API keys*

## Components
### Hardware Technologies
* Type of dispenser: Bubble gum dispenser or cereal dispenser or make my own dispenser from cardboard?  Bubble gum dispenser much cheaper but need coin for most and harder to trigger release mechanism. Cereal dispenser medium price but motor rotation piece looks like it may fit right on the handle. *I ended up using the cereal dispenser and the motor fit as expected*
* Servo Motor attachment: Use either a screw, bolt and U component or hold it in place with 3m extra strength double sided tape, L bracket 2 inches long, spacer and zip ties – might be easier and less risk to the dispenser. *I used the L Bracket which fit perfectly, the spacer and the tape with zip ties*
* Handle turn degree? *30 degrees seems about right*
* Raspberry Pi - *CanaKit Raspberry Pi 3 Ultimate Starter Kit - 32 GB Edition with power supply*
* PiCamera - First picamera did not work so used *Arducam Octoprint Octopi Webcam, Monitor 3D Printer, 3.28FT/100CM Long Extension Flex Ribbon Cable* which did work.

### Software Technologies
* Messaging service: Best option from research appears to be Twilio. Could also use IFTT technology though this appears to be more complex. *I used Twilio*
* Hosting platform: Ngrok or Heroku – Ngrok may be best for local hosting – faster and more reliable though if server shuts down software will fail. *I used Ngrok*
* Call Program to dispense treats: Twilio sms set to a webhook http callback which will execute a Flask app hosted on Ngrok – a tunnel web server forwarded from local host. User activates dispenser by texting 'yes' or 'treats' (no case sensitivity) to the App phone number. A reply will be generated if app is successful telling the user that their pet thanks them for the treats. *See below for unit tests*.
*Image Hosting Platform – Cloudinary – I already had an account.

### Testing Connections
1. Test that the servo motor control horn fits nicely into the handle of the cereal dispenser - had to remove a plastic bump on the handle and used the four prong rotation piece. Drilled it in and used the screws provided with the motor to secure it. Ran a servo motor software program to test motor rotation.  
2. Test that the Twilio App can send a message to the user - set up a phone number and ran their test code to my phone number and it worked.
3. Test that the Twilio App can receive messages from the user - this was more complex and involved setting up an https webhook hosted on Ngrok to forward sms replies. Based on the sms content the dispenser will be activated.  Flask app is hosted on port 5000.
4. Test that cat can get at treats - I needed to make a ramp out of paper so the treats could slide out and he could get them. I also had to secure the device to the desk using a desk clamp and duct tape so that the cat couldn't knock it over. Also secured the picamera.
5. Test that the picamera works and can snap and save an image to the local drive. 
6. Test Cloudinary to save that image online so that it can be sent along with the reply text message to the user as an MMS. Make sure all caching and versioning is removed.
7. Test config.ini file and config parser can manage all api keys.

## Wireframes

![Hardware Wireframe](https://i.ibb.co/RP1qCVB/treat-dispenser-hardware-design-d-sleeper.jpg)

![Software Wireframe](https://i.ibb.co/4mx83Hn/treat-dispenser-software-design-d-sleeper.jpg)

## Full Video of the App in action! Click the link below the still image.

![Full Video of Treat App](https://i.ibb.co/x6QbsfR/Image-from-i-OS.png)](https://streamable.com/phfr3z)

## Screenshots of Making the Project

**Realizing we need to lock down the dispenser**

![Cat Attack](https://i.ibb.co/DD11yKQ/Image-from-i-OS-2.png)

**Screwing servo motor into the dispenser handle**

![Drill](https://i.ibb.co/2k1vvrx/Image-from-i-OS-1.png)

![Screw](https://i.ibb.co/fY55PzJ/Image-from-i-OS-4.png)

**Attaching the Servo Motor to the dispenser so it won't move but the control horn will**

![Motor Attached](https://i.ibb.co/vVVz4P0/Image-from-i-OS-5.png)

**Attaching the Picamera so that pet can be captured in the photo**

![Picamera Attached](https://i.ibb.co/K5kdd2Y/Image-from-i-OS-2.jpg)

**Also made a new ramp out of a postcard and toilet paper role that cat could not tear**

![Cat getting pic taken](https://i.ibb.co/92mYFJx/Image-from-i-OS-1.jpg)

**Screenshot of what text messages and photos to and from the Twilio account**

![Twilio](https://i.ibb.co/CmLGFw7/IMG-9578.jpg)
