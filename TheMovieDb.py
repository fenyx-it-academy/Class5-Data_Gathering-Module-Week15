import json
import requests
from requests.models import Response, requote_uri
import time
class Themoviedb:
    def __init__(self):
        self.url = "https://api.themoviedb.org"
        with open('api_key.json', 'r') as jsFile:
            data = json.load(jsFile)
        self.api_key = data["api_key"]

    def search(self,keyword):
        get = requests.get(self.url+'/3/search/movie?api_key='+self.api_key+'&query='+keyword)
        print(self.url+'/3/search/movie?api_key='+self.api_key+'&query='+keyword)
        return get.json()

    def popularMovie(self):
        get = requests.get(self.url+'/3/movie/popular?api_key='+self.api_key)
        return get.json()

    def tredingMovie(self):
        get = requests.get(self.url+'/3/trending/movie/week?api_key='+self.api_key)
        return get.json()

    def first33Movie(self,page):
        get = requests.get(self.url+'/3/movie/top_rated?api_key='+self.api_key+'&page='+n)
        return get.json()

    def rateMovie(self,movie_id,rate_value):
        session_id = requests.get(self.url+'/3/authentication/guest_session/new?api_key='+self.api_key).json()['guest_session_id']
        get = requests.post(self.url+'/3/movie/'+movie_id+'/rating?api_key='+self.api_key+'&guest_session_id='+session_id,json={
            'value':rate_value
            })
        return get.json()
    def getMovieInfo(self,movie_id):
        get = requests.get(self.url+'/3/movie/'+movie_id+'?api_key='+self.api_key)
        return get.json()




themovie = Themoviedb()
while True:
    print("""
        Menu:
            1.Search a Movie
            2.the most popular movies
            3.10 of the trending weekly movies
            4.first 33 movies
            5.rate
            6.exit
        """)
    choise = input("Enter your choise:")
    if choise == "1":
        keyword = input("Enter keyword: ")
        keyword = keyword.replace(" ", "%20")
        result = themovie.search(keyword)
        for i in result['results']:
            print(f"ID : {i['id']}\nName : {i['title']}")
            print("*********************************")
        
    elif choise =="2":
        result = themovie.popularMovie()
        for i in result['results']:
            print(f"""
            title: {i['title']}
            popularity: {i['popularity']}
            release_date: {i['release_date']}
            vote_average: {i['vote_average']}
            *********************************
            """)
        
    elif choise == "3":
        result = themovie.tredingMovie()
        j = 0
        for i in result['results']:
            if j<10:
                j+=1
                print(f"""
                    --{j}--
            title: {i['title']}
            popularity: {i['popularity']}
            release_date: {i['release_date']}
            vote_average: {i['vote_average']}
            *********************************
                """)
            else:
                break

    elif choise == "4":
        n="1"
        j =0
        if j<20:
            result = themovie.first33Movie(n)
            for i in result['results']:
                j+=1
                print(f"""
                    --{j}--
            title: {i['title']}
            popularity: {i['popularity']}
            release_date: {i['release_date']}
            vote_average: {i['vote_average']}
            *********************************
                """)
        if j >=20:
            n="2"
            result = themovie.first33Movie(n)
            for i in result['results']:
                if j < 33:
                    j+=1
                    print(f"""
                        --{j}--
            title: {i['title']}
            popularity: {i['popularity']}
            release_date: {i['release_date']}
            vote_average: {i['vote_average']}
            *********************************
                """)
    
                else:
                    break
        
    elif choise == "5":
        keyword = input("Enter keyword: ")
        result = themovie.search(keyword)
        keyword = keyword.replace(" ", "%20")
        # print(result)
        for i in result['results']:
            print(f"""
                title: {i['title']}
                ID: {i['id']}
                vote_average: {i['vote_average']}
                *********************************
                    """)
        while True:
            try:
                movie_id = int(input("please,enter the id of movie which you want to rate: "))
                movie_id = str(movie_id)
                break
            except:
                print("Input errors, please try again.")
        movie_info = themovie.getMovieInfo(movie_id)
        print(f"""The movie you want to rate is:
                ID:{movie_info['id']}
                title:{movie_info['title']}
                release_date: {movie_info['release_date']}
                vote_average: {movie_info['vote_average']}
                *********************************
                """)
        while True:
            try:
                my_rating = float(input("Enter 0 for back to menu\nRate this movie(0.5~10.0): "))
                if 0.5 <= my_rating <=10.0:
                    if my_rating%0.50==0.0:
                        break
                    else:
                        print("Value invalid: Values must be a multiple of 0.50.")
                elif my_rating== 0:
                    break
                else:
                    print("Please,enter the rating between 0.5~10.0")
            except:
                print("Input errors, please try again.")
        result = themovie.rateMovie(movie_id,my_rating)
        print(result['status_message'],'\nYour rating has been saved.')
    elif choise == "6":
        break
    else:
        print("Input errors, please try again.")
    