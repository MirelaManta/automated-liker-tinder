# Tinder Auto Liker

This project is an automation script written in Python, using Selenium, that logs into your Tinder account using Facebook credentials, and automatically swipes right (i.e., "likes") 100 profiles in succession, allowing you to easily find matches.
## Installation
To run this script, you need to have the following libraries installed:
* Selenium
* python-dotenv

You also need to have __Google Chrome__ installed on your machine, download the __ChromeDriver__ executable and update the __chrome_driver_path__ variable in the script with the path of the ChromeDriver executable.

To install the required libraries, open your command prompt and run:
```
pip install selenium python-dotenv
```
## Usage

Before running the script, you need to set your Facebook phone number and password as environment variables. You can do this by creating a .env file in the root directory of the project and adding the following lines:
```
FB_PHONE=your_facebook_phone_number
FB_PASS=your_facebook_password
```
Once you have set your environment variables, you can run the script by navigating to the root directory of the project and running:
```
python main.py
```
The script will open Google Chrome and automatically log into your Tinder account using your Facebook credentials. After granting location access and accepting cookies, the bot will start liking profiles automatically, allowing you to easily find matches.  
___Note: Tinder free tier only allows 100 likes per day. After 100 likes, the code will stop executing. You can run the project again the next day to continue liking profiles.___
