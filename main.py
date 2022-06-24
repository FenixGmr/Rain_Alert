import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
# import smtplib

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWN_API_KEY ")
account_sid = "Code"
auth_token = "your_auth_token"

MY_LAT = 26.324100 # Your latitude
MY_LONG = 94.521202 # Your longitude

weather_params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "exclude": "current,minutely,daily",
        "appid": api_key,
    }


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#         .create(
#         body="It's going to rain today. Remember to bring an ☔️",
#         from_="YOUR TWILIO VIRTUAL NUMBER",
#         to="YOUR TWILIO VERIFIED REAL NUMBER"
#     )
#     print(message.status)

    # connection = smtplib.SMTP("smtp.gmail.com")
    # connection.starttls()
    # connection.login(MY_EMAIL, MY_PASSWORD)
    # connection.sendmail(
    #     from_addr=MY_EMAIL,
    #     to_addrs=MY_PASSWORD,
    #     msg="Subject:Look Up\n\nThe ISS is above you in the sky"
    #
    # )
