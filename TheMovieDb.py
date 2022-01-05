import requests
class TheMovieDb:
    def __init__(self):
        self.api_url='https://api.themoviedb.org'
        self.api_key='****************' 
       
    def getsearch(self, keyword):
        #response = requests.get(self.api_url+'&query='+keyword)
        response=requests.get(self.api_url+'/3/search/movie?api_key='+self.api_key+'&query='+keyword)
        return response.json()

    def getpopular(self):
        response=requests.get(self.api_url+'/3/movie/popular?api_key='+self.api_key)
        return response.json()

    def gettrending(self):
        response=requests.get(self.api_url+'/3/trending/movie/week?api_key='+self.api_key)
        return response.json()

    def getfirst33(self):
        response=requests.get(self.api_url+'/3/movie/top_rated?api_key='+self.api_key)
        response2=requests.get(self.api_url+'/3/movie/top_rated?api_key='+self.api_key +'&page=2')
        list = [response.json(), response2.json()]
        return list

    def rateamovie(self, movieid, rating):
        self.guest_session_id = requests.get(self.api_url+ '3/authentication/guest_session/new?api_key='+self.api_key).json()['guest_session_id']     
        response=requests.post(self.api_url+'/3/movie/'+movieid+'/rating?api_key='+self.api_key+'&guest_session_id='+self.guest_session_id, json={'value':rating})
        return response.json()

movie=TheMovieDb()
while True:
    secim = input('1- Search\n2- The most popular movie list\n3- 10 of the trending weekly movies\n4- The list of the first 33 movies\n5- Rate a movie\n6- Exit\nSeçim: ')
    if secim == '6':
        break
    else:
        if secim == '1':
            keyword = input('Keyword: ')
            result = movie.getsearch(keyword)
            for i in result["results"]:
                print(f"ID:{i['id']}\nName:{i['original_title']}\n")

        if secim == '2':
            result = movie.getpopular()
            for i in result["results"]:
                print(f"title:{i['title']}\npopularity:{i['popularity']}\nrelease_date:{i['release_date']}\nvote_average:{i['vote_average']}\n")

        if secim == '3':
            result = movie.gettrending()
            for i in result["results"][:10]:
                print(f"title:{i['title']}\npopularity:{i['popularity']}\nrelease_date:{i['release_date']}\nvote_average:{i['vote_average']}\n")

        if secim == '4':
            result = movie.getfirst33()
            for i in result[0]["results"]:
                print(f"title:{i['title']}\npopularity:{i['popularity']}\nrelease_date:{i['release_date']}\nvote_average:{i['vote_average']}\n")
            for i in result[1]["results"][:13]:
                print(f"title:{i['title']}\npopularity:{i['popularity']}\nrelease_date:{i['release_date']}\nvote_average:{i['vote_average']}\n")

        if secim == '5':
            movieid = input('Enter the movie ID:')
            rating = input('The rating value (between 0.5 and 10.0.):')
            result = movie.rateamovie(movieid, rating)
            print(result['status_message'])
