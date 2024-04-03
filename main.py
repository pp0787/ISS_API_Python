import requests
from datetime import datetime
import smtplib



MY_LAT = -30.507351 # Your latitude
MY_LONG = -130.127758 # Your longitude
my_email="priyankubain@gmail.com"
my_password="xyoumjbdidoblkzg"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# print(iss_latitude)
# print(iss_longitude)
#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
# print(time_now.hour)
# print(sunrise)
# print(sunset)
# print(time_now)
# print(iss_longitude - MY_LONG)
# print(iss_latitude - MY_LAT)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
if (-5<= iss_latitude - MY_LAT <=5) and (-5<= iss_longitude - MY_LONG <=5) and time_now.hour>sunrise:
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as connection:
        connection.starttls()

        connection.login(user=my_email,password=my_password)

        subject = "Subject: ISS Overhead"
        email_message = f"{subject}\n\n Lookup for ISS"

        connection.sendmail(from_addr=my_email,to_addrs="ppant0787@gmail.com",msg=email_message)



