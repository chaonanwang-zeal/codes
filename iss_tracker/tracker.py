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
    # if (longitude >= MY_LNG - 5 and longitude <= MY_LNG + 5) and (latitude >= MY_LAT - 5 and latitude <= MY_LAT + 5):
    #    return True
    # for test
    return True



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
    # if time_now.hour >= sunset_date.hour or time_now.hour <= sunrise_date.hour:
    #     return True
    # for test
    return True

def email_yourself():
    pass

res1 = iss_over_head()
res2 = is_night()

print(res1, res2)
