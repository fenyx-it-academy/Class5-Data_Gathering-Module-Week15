import requests

class Imbd:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org'
        self.api_key = '**************************'

    def Search(self,movie_id):
        response=requests.get(self.api_url+f'/3/movie/{movie_id}/keywords?api_key='+self.api_key)
        return response.json()


    def Most_p_m(self):
        response = requests.get(self.api_url+'/3/movie/popular?api_key='+self.api_key,'language=en-US&page=1')    
        return response.json()

    def Trending_weekly(self):
        response=requests.get(self.api_url+'/3/trending/movie/week?api_key='+self.api_key)
        return response.json()
    
    def Top_rated_33(self):
        response=requests.get(self.api_url+'/3/movie/top_rated?api_key='+self.api_key,'language=en-US&page=1')
        return response.json()
    
    def Top_rated_33_2(self):
        response=requests.get(self.api_url+'/3/movie/top_rated?api_key='+self.api_key,'language=en-US&page=2')
        return response.json()
        
    def Movie_rating(self,movie_id,rate):
        response=requests.post(self.api_url+f'/3/movie/{movie_id}/rating?api_key='+self.api_key, json = {
                "value": f'{rate}'
        })
        return response.json()

imbd = Imbd()


while True:
    choice=input('1) Search\n2) Most Popular Movies\n3) 10 of the Trending Weekly Movies\n4) First 33 Movies\n5) Movie Rating\n6) Exit\nPlease enter a number from 1 to 6!: ')
    
    if choice=='6':
        break
    else:
        if choice == '1':
            movie_id = input("Please enter a movie id: ")
            counter = 0
            while counter < 20:
                result = imbd.Search(movie_id)['keywords'][counter]
                counter += 1
                print(f"ID: {result['id']}\nName: {result['name']} ")
                print("################TheMovieDb################")

        elif choice == '2':
            counter = 0
            while counter < 20:
                result = imbd.Most_p_m()['results'][counter]
                counter += 1
                print(f"Title: {result['title']}\nPopularity: {result['popularity']}\nRelease Date: {result['release_date']}\nVote Average: {result['vote_average']} ")
                print("################TheMovieDb################")

        elif choice == '3':
            counter = 0
            while counter < 10:
                    result = imbd.Trending_weekly()["results"][counter]
                    counter += 1
                    print(f"Title: {result['title']}\nPopularity: {result['popularity']}\nRelease Date: {result['release_date']}\nVote Average: {result['vote_average']} ")
                    print("################TheMovieDb################")

        elif choice == '4':
            counter = 0
            while counter < 20:
                    result = imbd.Top_rated_33()["results"][counter]
                    counter += 1
                    print(f"Title: {result['title']}\nPopularity: {result['popularity']}\nRelease Date: {result['release_date']}\nVote Average: {result['vote_average']} ")
                    print("################TheMovieDb################")
                    continue
            response_ = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=e93dde24653daac0d72c830bebc1a45a&language=en-US&page=2")
            counter = 0
            while counter < 13:
                    result = imbd.Top_rated_33_2()["results"][counter]
                    counter += 1
                    print(f"Title: {result['title']}\nPopularity: {result['popularity']}\nRelease Date: {result['release_date']}\nVote Average: {result['vote_average']} ")
                    print("################TheMovieDb################")

        elif choice == '5':
            movie_id = input("Please enter a movie id: ")
            rate = input("Please enter a rate: ")
            result = imbd.Movie_rating(movie_id,rate)
            print(result)
            
        else:
            print('Your choice is wrong! Please try a valid number!') 