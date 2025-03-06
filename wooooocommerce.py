from time import sleep
from woocommerce import API
import json
from dateutil import parser
import os
from datetime import datetime

ds = "2012-03-01T10:00:00Z"  # or any date sting of differing formats.
date = parser.parse(ds)
from playsound import playsound


SOUND_FILENAME = "sound.wav"
SPECIAL_SOUND_FILENAME = "special_sound.wav"
FAST_SHIPPING_FILENAME = "fast_sound.wav"
FAST_SPECIAL_SHIPPING_FILENAME = "fast_special_sound.wav"
sound = None
specialsound = None
fastsound = None
fastspecialsound = None

# sound settings
# 24 hour notation
no_sound_before = 11
no_sound_after = 18

# if the order total (excl. shipping) is greater than this value,
# play the special sound
magic_value = 250

# change working directory to this folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# check if sound.wav exists
try:
    open(SOUND_FILENAME, "r")
    sound = True
except IOError:
    print("Audio file not found")
    sound = None

# check if special_sound.wav exists
try:
    open(SPECIAL_SOUND_FILENAME, "r")
    specialsound = True
except IOError:
    print("Special audio file not found")
    specialsound = None

try:
    open(FAST_SHIPPING_FILENAME, "r")
    fastsound = True
except IOError:
    print("Fast shipping audio file not found")
    fastsound = None

try:
    open(FAST_SPECIAL_SHIPPING_FILENAME, "r")
    fastspecialsound = True
except IOError:
    print("Fast special shipping audio file not found")
    fastspecialsound = None

# get secret keys from file
with open("keys.json") as f:
    keys = json.load(f)
    url = keys["url"]
    consumer_key = keys["consumer_key"]
    consumer_secret = keys["consumer_secret"]

print("Started, checking for new orders...")


while True:
    try:
        wcapi = API(
            url=url,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            version="wc/v3",
        )

        # create file if it doesn't exist
        with open("last_order.txt", "a+") as f:
            pass

        latest_order = wcapi.get("orders").json()[0]
        latest_order_str = latest_order["date_created"]
        latest_order_time = parser.parse(latest_order["date_created"])
        shipping_method = latest_order["shipping_lines"][0]["method_title"]
        fastshipping = not "free" in shipping_method.lower()

        # read previous last order
        with open("last_order.txt", "r") as f:
            prev_last_order_str = f.read()
            try:
                if (
                    parser.parse(prev_last_order_str) < latest_order_time
                    and latest_order['status'] == "processing"
                ):
                    print("new order!!!")
                    specialorder = float(latest_order['total']) - float(latest_order['shipping_total']) > magic_value
                    if sound and no_sound_before <= datetime.now().hour < no_sound_after:
                        if fastshipping and fastsound:
                            if specialorder and fastspecialsound:
                                playsound(FAST_SPECIAL_SHIPPING_FILENAME)
                            else:
                                playsound(FAST_SHIPPING_FILENAME)
                        elif specialorder and specialsound:
                            playsound(SPECIAL_SOUND_FILENAME)
                        else:
                            playsound(SOUND_FILENAME)
                    # write new last order
                    with open("last_order.txt", "w") as f:
                        f.write(latest_order_str)
                # else:
                #     print('no new order....')
                #     print('yet!')
            except ValueError as e:
                print("no valid previous order found")
                with open("last_order.txt", "w") as f:
                    f.write(latest_order_str)
    except Exception as e:
        print(e)
        print("error, trying again in 5 seconds...")
    sleep(5)
