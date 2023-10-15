# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S3vcCvWtRoKIv3HKYWSKhILfFTn38OWl
"""

#Description : This prorgam is for happy birthday email from a list of birthdays to your friends!!!

#lets import some libraries
import datetime
import pandas as pd
import numpy as mp
import smtplib
import ssl
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM

#load the birthday list data!!
from google.colab import  files
files.upload()

# read the data
df = pd.read_excel('birthday.xlsx')
#Show the data
df

#Creat a funtion to send email

def email_func(subject,birthday_receiver,name,):

  #store the email address for the recevier and the sender also store the senders email passowrdd
  receiver = birthday_receiver
  sender = 'dontknowsam413@gmail.com'
  sender_password = 'bpuf brdx pufe mrgm'

  #create a mimemultipart object
  msg= MM()
  msg ['Subject'] = subject+' '+str(name)+'!'

  #Create the HTML for the mesge!!
  HTML = """
  <html>
  <body>
  <h1>HAPPY BIRTHDAY! </h1>
  <img src="https://avante.biz/wp-content/uploads/Happy-Bday-Images-Wallpapers/Happy-Bday-Images-Wallpapers-055.jpg" alt="Image" width="640" height="360"></img>
  <p>Photo by: Sameer </p>
  <h2>
  <p>
  Hellom<br>
  I Hope you have a wonderful day today! <br> <br>
  From;<br>
  Your Friend
  </p>
  </h2>

  </body>
  </html>
  """


  #Create a MIMEText Object!
  MTObj = MT(HTML,  "html")

  #Attack the MimeTetxt obj into the mesge container!!
  msg.attach(MTObj)

  #create a scure connection with server tto send a emial!!
  #here we are going to create ssl layer

  SSL_context = ssl.create_default_context()

  #create the server simple mail transfewr protocol SMTP connection!

  server = smtplib.SMTP_SSL(host='smtp.gmail.com',port=465,context=SSL_context)


  #login to the email account
  server.login(sender,sender_password)

  #SEND TGHER EMAIL
  server.sendmail(sender,receiver,msg.as_string())

#get todays date

today = datetime.date.today()

#get the curent year
year = today.year

#loop through the birthday list to send the mail according to birthday!!!

for i in range(0,len(df)):

  #get the person month
  month = df['Birth_Month'][i]

  #get the person date of birth
  day = df['Birth_day'][i]

  #get the person name
  name = df['Name'][i]

  #get the person email address
  email= df['Email'][i]

  #get the person birthdate
  birthdate = datetime.date(year, month, day)

  #check if today is birthday or not

  if birthdate == today:
    email_func('Happy Birthday',email,name)
    print('Sent Happy Bithday')
  else:
    print("Did not send")