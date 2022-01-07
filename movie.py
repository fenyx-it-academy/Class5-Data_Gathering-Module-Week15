import requests

class Movie:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org'
        self.apiKey = '****************************'

    def search(self,keyword):
        response=requests.get(self.api_url+'/3/search/movie?api_key='+self.apiKey+'&query='+keyword)
        return response.json()

    def popular_movie(self):
        response = requests.get(self.api_url+'/3/movie/popular?api_key='+self.apiKey)
        return response.json()
    
    def weekly_trend(self):
        response = requests.get(self.api_url+'/3/trending/movie/week?api_key='+self.apiKey)
        return response.json()

    def highest_score(self):
        response=requests.get(self.api_url+'/3/movie/top_rated?api_key='+self.apiKey+'&page=2')
        return response.json()
    def rate(self,movie_id,rating):
        session_id = requests.get(self.api_url+'/3/authentication/guest_session/new?api_key='+self.apiKey).json()['guest_session_id']
        get = requests.post(self.api_url+'/3/movie/'+movie_id+'/rating?api_key='+self.apiKey+'&guest_session_id='+session_id,json={
            'value':rating
            })
        return get.json()

movie = Movie()

while True:
    secim = input('1- Search\n2- popular_movie\n3- weekly_trend\n4-highest_score\n5-rate\n6- Exit\nSeçim: ')

    if secim == '6':
        break
    else:
        if secim == '1':
            keyword= input('keyword: ')
            result = movie.search(keyword)
            for i in result['results']:
                print(f"Name: {i['title']}\nID: {i['id']}")

        elif secim == '2':
            result = movie.popular_movie()
            for i in result['results']:
                print(f"Title:{i['title']}\nPopularity:{i['popularity']}\nRelease_Date:{i['release_date']}\nVote_average:{i['vote_average']}")

        elif secim == '3':
            result = movie.weekly_trend()
            for i in result['results'][:10]:
                print(f"Title:{i['title']}\nPopularity:{i['popularity']}\nRelease_Date:{i['release_date']}\nVote_average:{i['vote_average']}")
        
        elif secim == '4':
            result=movie.highest_score()
            for i in result['results']:
                print(f"Title:{i['title']}\nPopularity:{i['popularity']}\nRelease_Date:{i['release_date']}\nVote_average:{i['vote_average']}")
        elif secim == '5':
            movie_id=input("Please enter your movie id: ")
            rating=input("Please enter a rating(minimum:0.5,maximum:10): ")
            result=movie.rate(movie_id,rating)
            print(result)

        
        else:
            print('yanlış seçim') 