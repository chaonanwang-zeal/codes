# pip install requests
import requests
from datetime import datetime, timedelta


# https://www.latlong.net/   get the Tokyo position
MY_LAT = 35.689487
MY_LNG = 139.691711


def iss_over_head():
    # get date from the iss station api
    url = "http://api.open-notify.org/iss-now.json"
    responses = requests.get(url=url)
    responses.raise_for_status()
    data = responses.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    if (longitude >= MY_LNG - 5 and longitude <= MY_LNG + 5) and (latitude >= MY_LAT - 5 and latitude <= MY_LAT + 5):
        return True
    return False
# longitude and latitude can address a position on the earth.
# use this: https://www.latlong.net/Show-Latitude-Longitude.html


# get local sunrise and sunset time, so you can know if is dark enough to see the station.
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    # Thank you !stackoverflow!
    # https://stackoverflow.com/questions/69334328/how-do-i-convert-an-api-utc-time-to-local-time-1300
    sunrise_date = datetime.fromisoformat(sunrise) + timedelta(hours=9)
    sunset_date = datetime.fromisoformat(sunset) + timedelta(hours=9)
    time_now = datetime.now()
    if time_now.hour >= sunset_date.hour or time_now.hour <= sunrise_date.hour:
        return True
    # this make things more smart than the lesson!!!great!
    # print(sunrise_date)
    # print(time_now)

# if the ISS is close to my current position.
# if (longitude >= MY_LNG - 5 and longitude <= MY_LNG + 5) and (latitude >= MY_LAT - 5 and latitude <= MY_LAT + 5):
#     if time_now.hour >= sunset_date.hour or time_now.hour <= sunrise_date.hour:
#         print("look up!")
#     else:
#         print("can not see.")
# else:
#     print("nothing.")
# if it is currently dark.
# Pass: send a email to see "look up!",run it on the cloud to check.


def email_yourself():
    pass

res1 = iss_over_head()
res2 = is_night()

print(res1, res2)

# if iss_over_head() and is_night():
#     print("Look up!")
#     email_yourself()
