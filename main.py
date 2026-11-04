import requests
import os
import smtplib
my_email=os.environ.get("MY_EMAIL")
password=os.environ.get("PASSWORD")
api_key=os.environ.get("API_KEY")
parameters = {
    "appid":api_key,
    "lat":41.4843023,
    "lon":37.7322878,
    "cnt":4
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain=False
for dt in data["list"]:
    if int(dt["weather"][0]["id"])<700:
        will_rain=True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="udemysendertest@gmail.com",
                            msg=f"Subject:Weather\n\n Bring an umbrella.")
    print("Bring an umbrella.")
