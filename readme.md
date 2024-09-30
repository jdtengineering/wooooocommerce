# Wooooocommerce

Play a sound everytime someone bought something on your Woocommerce shop, woooooo! (That's 5 o's)

How to use:
Create a webhook in woocommerce and add you consumer key and secret to a file called `keys.json`. Also add your website's url to the file. For example:

Everytime the script run, it fetches the date of the last order that has status "processing". If that date is newer than the previous last date, it must be a new order!

### Requirements
- Python 3
- pip
- virtualenv (not strictly needed)

### Installation
```virtualenv venv
venv\Scripts\activate
pip install -r requirements
```

### Configuring Woocommerce
Go to Woocommerce settings > Advanced

![add rest api key](https://github.com/user-attachments/assets/e8c5b0c5-03bf-414d-996a-50e3ee4b5e54)

 Create new keys
 
![key details](https://user-images.githubusercontent.com/8831830/195899932-f1840d55-948b-4bca-b849-679b9c708f8a.png)

Copy these keys to `keys.json`. Don't share these with anyone else!

![new details](https://user-images.githubusercontent.com/8831830/195899945-92a6b997-8f0d-4c9f-be49-fdff5979d959.png)

### Using
Make sure to put your webhook keys and website url in `keys.json`:

```
{
    "url": "https://example.com",
    "consumer_key": "your_key",
    "consumer_secret": "your_secret"
}
```

Then run the script by:
```
venv\Scripts\activate
python wooooocommerce.py
```

### How to install as service on Ubuntu Linux
Copy `wooooocommerce.service` to `/etc/systemd/system/`

Edit the file and replace USERNAME with your Linux username

Type this into your terminal to enable the systemd service

```
sudo systemd daemon-reload
sudo systemctl start wooooocommerce.service
``` 
