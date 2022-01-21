import requests
import json
from datetime import date

class Fear_Greed:
    '''class to Read from bitcoin fear and greed index'''
    def __init__(self, name, time, value, classification):
        
        
        self.name = name
        self.time = time
        self.value = value
        self.classification = classification
        
    def print_info():
        '''Method to print the data from  Fear and greed index for bitcoin'''
        uri = 'https://api.alternative.me/fng/?limit=2'
        today = date.today()
        d1 = today.strftime("%m/%d/%Y")

        r = requests.get(uri) 
        data = r.json()
        #def find_actors(self, movies):
        with open('output.json', 'w') as file:
            file.write(f"{data}")
        name = data['name']
        time = data['data'][0]['timestamp']
        value = data['data'][0]['value']
        classification = data['data'][0]['value_classification']
        endline = "\n-----------------------------\n"
        print(f"{name}\n\n\tFear level: {value}\n\tRating: {classification}\n\tTimestamp: {time}\n\tDate: {d1}\n{endline}")
print(Fear_Greed.print_info())
