import requests

class TheMovieDB:
    def __init__(self) -> None:
        self.api_url='https://api.themoviedb.org'
        self.api_key='**************************'
        self.guest_session_id=requests.get(self.api_url+'/3/authentication/guest_session/new?api_key='+self.api_key).json()['guest_session_id']
    def Search(self,Keyword,page='1'):
        response=requests.get(self.api_url+'/3/search/movie?api_key='+self.api_key+'&query='+Keyword+'&page='+page)
        return response.json()
    def Popular(self,page='1'):
        response=requests.get(self.api_url+'/3/movie/popular?api_key='+self.api_key+'&page='+page)
        return response.json()
    def Trends_Week(self):
        response=requests.get(self.api_url+'/3/trending/movie/week?api_key='+self.api_key)
        return response.json()
    def Highest_33_Movies(self,page):
        response=requests.get(self.api_url+'/3/movie/top_rated?api_key='+self.api_key+'&page={}'.format(page))
        return response.json()
    def Rate_Movie(self,movie_id,rating):
        response=requests.post(self.api_url+'/3/movie/'+movie_id+'/rating?api_key='+self.api_key+'&guest_session_id='+self.guest_session_id,json={'value':rating})
        return response.json()

the=TheMovieDB()




while True:
    choice=input('1- Search\n2- Get Most Popular Movies\n3- 10 of the Trending Weekly Movies\n4- The List of the First 33 Movies with the Highest Score\n5- Rate a Movie\n6- Exit\nChoice: ')
    if choice=='6':
        break
    else:
        if choice=='1':
            search=input('Search: ')
            result=the.Search(search)
            total_page=result['total_pages']
            for i in range(1,total_page+1):
                result=the.Search(search,str(i))
                for i in result['results']:
                    print("""
    ID: {}
    Name: {}
    ______________________________________""".format(i['id'],i['original_title']))
        elif choice=='2':
            result=the.Popular()
            total_page=1
            for i in range(1,total_page+1):
                result=the.Popular(str(i))
                for i in result['results']:
                    print("""
    title: {}

    popularity: {}

    release_date: {}

    vote_average: {}

    ______________________________________""".format(i['title'],i['popularity'],i['release_date'],i['vote_average']))
        elif choice=='3':
            result=the.Trends_Week()
            for i in result['results'][:10]:
                print("""
    title: {}

    popularity: {}

    release_date: {}

    vote_average: {}

    ______________________________________""".format(i['title'],i['popularity'],i['release_date'],i['vote_average']))
        
        elif choice=='4':
            show=0
            total_page=33//20+1
            for k in range(0,total_page):
                result=the.Highest_33_Movies(str(k+1))
                for i in result['results']:
                    show+=1
                    if show==34:
                        break
                    print("""
    title: {}

    popularity: {}

    release_date: {}

    vote_average: {}

    ______________________________________""".format(i['title'],i['popularity'],i['release_date'],i['vote_average']))

        elif choice=='5':
            movie_id=input('Movie id: ')
            rating=input('Rating(min 0.5- max 10): ')
            result=the.Rate_Movie(movie_id,rating)
            print(result['status_message'])