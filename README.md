## This is an sms sending Application for Africas Talking Company

- First of all, make sure you can be able to access the africastalking Python API.
  -> Regiester with the company.
  -> Go to the API section and work on it on your favourite IDE.
- After ascertaining that the raw API can send texts (on your sandbox simulated phone),
  then you are good to go to start developing an application using Django.
  -> Make sure you are able to access your username on the sandbox for testing and api_key.
  -> Also don't forget to generate a sender_id, this will be your code for sending texts.
- Now, build a Django app as illustrated by my application above.

## Make the App functional using Ngrok

- You will not see the text sent to your sandbox simulated phone nor the JSON response
  that the app was sent if you haven't deployed your app.
- Use Ngrok to solve this issue, a software application that makes your app go live for 2 hours
  and also gives you a callback url, which you can use on the SMS sandbox to receive messages.
- Try it out!
