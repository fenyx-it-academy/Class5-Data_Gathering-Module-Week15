import requests

class Movie:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org' 
        self.api_key = 'empty'#:)
        self.session_id = requests.get(self.api_url+'/3/authentication/guest_session/new?api_key='+self.api_key).json()['guest_session_id']#guest session id

    def search(self,keyword,page='1'):
        response = requests.get(self.api_url+'/3/search/movie?api_key='+self.api_key+'&query='+keyword+'&page='+ page)
        return response.json()
    def popular(self,page ='1'):
        response = requests.get(self.api_url+'/3/movie/popular?api_key='+self.api_key+'&page='+page)
        return response.json()
    def trendy(self,page='1'):
        response = requests.get(self.api_url+'/3/trending/movie/week?api_key='+self.api_key+'&page='+page)
        return response.json()
    def high_rated(self,page):
        response = requests.get(self.api_url+'/3/movie/top_rated?api_key='+self.api_key+'&page='+page)
        return response.json()
    def rate_movie(self,movie_id,rating):
        response = requests.post(self.api_url+'/3/movie/'+movie_id+'/rating?api_key='+self.api_key+'&guest_session_id='+self.session_id,json={'value':rating})
        return response.json()
        




movie = Movie()

while True:
    choice = input('1- FInd movie\n2- popular movies\n3-weeklytrend movies\n4-high_rated\n5-rate a movie\n6-exit')

    if choice == '6':
        break
    elif choice == '1':
        find = input('find:')
        result = movie.search(find)
        total_page = result['total_pages']
        for k in range(1,total_page+1):
            result = movie.search(find,str(k))#page parameter = k
            for i in result['results']:
                print("ID : {}\nNAME :{}\n".format(i['id'],i['original_title']))
    elif choice == '2':
        result = movie.popular()
        page = 1
        for k in range(1,page+1):
            result= movie.popular(str(k))#page parameter = k
            for i in result['results']:
                print("title:{}\npopularity:{}\nrelease_date:{}\nvote_average:{}\n".format(i['title'],i['popularity'],i['release_date'],i['vote_average']))
    elif choice == '3':
        result = movie.trendy()
        for i in result['results'][:10]:#:10 = first ten of the result
                print("title:{}\npopularity:{}\nrelease_date:{}\nvote_average:{}\n".format(i['title'],i['popularity'],i['release_date'],i['vote_average']))
    elif choice == '4':
        number = 0 
        total_page = 33//20 + 1 #  one page includes 20 movies
        for k in range(0,total_page):
            result = movie.high_rated(str(k+1))# k ->def high_rated(page=k+1) 
            for i in result['results']:
                number += 1#first 33 high rated movie
                if number == 34:
                    break

                print("title:{}\npopularity:{}\nrelease_date:{}\nvote_average:{}\n".format(i['title'],i['popularity'],i['release_date'],i['vote_average']))
    elif choice == '5':
        movie_id = input('movie_id:')
        rating = input('rating:')
        result = movie.rate_movie(movie_id,rating)
        print(result)
    else:
        print("Enter one of the numbers that are shown in the menu")
        



        

        
        