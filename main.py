import requests
import datetime as dt
import smtplib
import time
my_email="meghanvenkat429@gmail.com"
my_password="gipudpxycnaedxcy"
my_lat=51.507351
my_lng=-0.127758
def is_iss_overhead:
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    longitude=float(data["iss_position"]["longitude"])
    latitude=float(data["iss_position"]["latitude"])
    if my_lat-5<=latitude<=my_lat+5 and my_lng-5<=longitude<=my_lng+5:
        return True
def is_night():
    paramaters={
        "lat":my_lat,
        "lng":my_lng,
        "formatted":0,
    }
    response=requests.get(url=" https://api.sunrise-sunset.org/json",params=paramaters)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now=dt.datetime.now()
    if time_now>=sunset or time_now<=sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="subject:Look up\n\nThe ISS is above you in the sky."
        )