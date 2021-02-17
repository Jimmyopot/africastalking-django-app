from django.db import models

import json
import requests


class Talking(models.Model):
    username = models.CharField(max_length=200, blank=True, null=True)
    api_key = models.CharField(max_length=201, blank=True, null=True)
    recepients = models.TextField(max_length=1000, blank=True, null=True)
    message = models.TextField(max_length=200, blank=True, null=True)
    sender_id = models.CharField(max_length=200, blank=True, null=True)
    
    
    def __str__(self):
        return self.username
    
    
    def save(self, *args, **kwargs):     

        url = 'https://api.sandbox.africastalking.com/version1/messaging'  # set url  
        
        headers = {
            'ApiKey': self.api_key, 
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        data = {
            'username': self.username,
            'from': self.sender_id,
            'message': self.message,
            'to': self.recepients,
        }
        
        def make_post_request():  
            response = requests.post(url=url, headers=headers, data=data )
            return response
        
            with open(r'C:/Users/user/projects/sendCemanet_sms/credit/templates/credit/report.html', 'w') as f:
                f.write(response.text)
                print(f)
        
        print( make_post_request().json() )

        return super(Talking, self).save(*args, **kwargs)