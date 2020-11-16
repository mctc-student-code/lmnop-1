import os
import requests
import re
from ..models import Artist, Venue, Show
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone #maybe not needed

#getting data from  ticketmaster api
key = os.environ.get('TICKETMASTER_KEY')
url = 'https://app.ticketmaster.com/discovery/v2/events'
classificationName = 'music'
city = 'Minneapolis'


def get_music_data(request):
    try:
        query= {'classificationName': classificationName, 'city' : city, 'apikey': key}
        response = requests.get(url, params=query)
        response.raise_for_status()  #will raise an exception for 400(client) or 500(server) errors
        data = response.json() 
        events = data['_embedded']['events']
        
        for event in events: 
            pattern = '[A-Za-z\s]{1,30}' #do I need r?
            performerLong = event['name']
            performerObj = re.search(pattern, performerLong)
            performer = performerObj.group()
            print(performer)
            venueName = event['_embedded']['venues'][0]['name']
            venueCity = event['_embedded']['venues'][0]['city']['name']
            venueState = event['_embedded']['venues'][0]['state']['stateCode']
            show_date = event['dates']['start']['localDate']   
            print(show_date)
         
           ##linking info to models and saving it
            new_artist = Artist(name=performer)
            new_artist.save()
            new_artist.id
            print('artistID',new_artist.id)
            
            new_venue = Venue(name=venueName, city=venueCity, state=venueState)
            new_venue.save()
            new_venue.id
            print('venueID', new_venue.id)

            new_show=Show(show_date=show_date, artist_id = new_artist.id, venue_id = new_venue.id)
            new_show.save()
            return HttpResponse('ok')
        
    except Exception as ex:
        print(ex)
       # logging.exception(ex)


