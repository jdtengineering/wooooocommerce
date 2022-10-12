from woocommerce import API
import json
from dateutil import parser
ds = '2012-03-01T10:00:00Z' # or any date sting of differing formats.
date = parser.parse(ds)

# get secret keys from file
with open('keys.json') as f:
    keys = json.load(f)
    consumer_key = keys['consumer_key']
    consumer_secret = keys['consumer_secret']
    # url = keys['url']

wcapi = API(
    url="https://howler-audio.com",
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    version="wc/v3"
)

# create file if it doesn't exist
with open('last_order.txt', 'a+') as f:
    pass

latest_order = wcapi.get('orders').json()[0]
latest_order_str = latest_order['date_created']
latest_order_time = parser.parse(latest_order['date_created'])

# read previous last order
with open('last_order.txt', 'r') as f:
    prev_last_order_str = f.read()
    try:
        if parser.parse(prev_last_order_str) < latest_order_time:
            print('new order!!!')
            # write new last order
            with open('last_order.txt', 'w') as f:
                f.write(latest_order_str)
        else:
            print('no new order....')
            print('yet!')
    except ValueError:
        print('no previous order found')
