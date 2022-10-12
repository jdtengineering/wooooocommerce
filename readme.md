Play a sound everytime someone bought something on your Woocommerce shop, woooooo!

How to use:
Create a webhook in woocommerce and add you consumer key and secret to a file called `keys.json`. Also add your website's url to the file. For example:

```
{
    "url": "https://example.com",
    "consumer_key": "your_key",
    "consumer_secret": "your_secret"
}
```

Everytime the script run, it fetches the date of the last order. If that date is newer than the previous last date, it must be a new order!

Currently, the script does not check if the order was actually succesful.

### Installation
```virtualenv venv
venv\Scripts\activate
pip install -r requirements
```

### Using
```
venv\Scripts\activate
python wooooocommerce.py
```
