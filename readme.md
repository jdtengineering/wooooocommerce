Play a sound everytime someone bought something on your Woocommerce shop, woooooo!

How to use:
Create a webhook in woocommerce and add you consumer key and secret to a file called `keys.json`. Also add your website's url to the file. For example:

Everytime the script run, it fetches the date of the last order. If that date is newer than the previous last date, it must be a new order!

Currently, the script does not check if the order was actually succesfull.

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

![add rest api key](https://user-images.githubusercontent.com/8831830/195899920-6fb44ec7-3c8c-4489-b13c-eafc6985be13.png)

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

```
venv\Scripts\activate
python wooooocommerce.py
```
