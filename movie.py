import requests

class Movie:
    def __init__(self):
        self.api_url="https://api.themoviedb.org"
        self.api_key="fd0ec3b81f8d0b51f74b537f50c64ea9"
        
        
    
    def getMovies(self,Keyword):
        response=requests.get(self.api_url+'/3/search/movie?api_key='+self.api_key+'&query='+Keyword)
        return response.json()
    
    def getPopular(self):
        response=requests.get(self.api_url+'/3/movie/popular?api_key='+self.api_key)
        return response.json()

    def getTrend(self):
        response=requests.get(self.api_url+'/3/trending/movie/week?api_key='+self.api_key)
        return response.json()
    
    def getHighest(self):
        response=requests.get(self.api_url+'/3/movie/top_rated?api_key='+self.api_key+'&page=2')
        return response.json()

    def giveRating(self,movie_id,rating):
        self.request_token=requests.get(self.api_url+'/3/authentication/token/new?api_key='+self.api_key)
        self.sension_id=requests.get(self.api_url+'/3/authentication/guest_session/new?api_key='+self.api_key+self.request_token)
        response =requests.post(self.api_url+'/3/movie/'+movie_id+'/rating?api_key='+self.api_key+'&quest_sension_id='+self.sension_id,json={'value':rating})
        return response.json()






movie=Movie()

while True:
    choice=input("1- Search Movie\n2- Most popular Movie\n3- Weekly trending 10 Movie\n4- 33 Movies with High score\n5- Rate a Movie\n6- Exit\nChoice: ")
    if choice=="6":
        break
    else:
        if choice =="1":
            Keyword=input("Keyword: ")
            result=movie.getMovies(Keyword)
            for i in result['results']:
               print(f"ID: {i['id']}\nName: {i['original_title']}\n--------------")
        
        if choice =="2":
            result=movie.getPopular()
            for i in result['results']:
                print(f"Title:{i['title']}\nPopularity:{i['popularity']}\nRelease_Date:{i['release_date']}\nVote_average:{i['vote_average']}\n-----------------")

        if choice =="3":
            result=movie.getTrend()
            for i in result['results'][:10]:
                print(f"Title:{i['title']}\nPopularity:{i['popularity']}\nRelease_Date:{i['release_date']}\nVote_average:{i['vote_average']}\n-----------------")
        
        if choice =="4":
            result=movie.getHighest()
            for i in result['results']:
                print(f"Title:{i['title']}\nPopularity:{i['popularity']}\nRelease_Date:{i['release_date']}\nVote_average:{i['vote_average']}\n-----------------")

        if choice =="5":
            movie_id=input("Please enter your movie id: ")
            rating=input("Please enter a rating(minimum:0.5,maximum:10): ")
            result=movie.giveRating(movie_id,rating)
            print(result)


             
            
               


        
            
