
import requests

class TheMovieDb:
    def __init__(self) -> None:
        self.api_url="https://api.themoviedb.org"
        self.api_key="d6576eff08d0b274dd0407f410df86b7"
        self.guest_session_ID=requests.get(self.api_url+'/3/authentication/guest_session/new?api_key='+self.api_key).json()['guest_session_id']

#Search should be made according to the "Keyword" requested from the user and the result will be printed on the screen with the following information
    def Search(self,keyword,page='1'):
       response=requests.get(self.api_url+'/3/search/movie?api_key='+self.api_key+'&query='+keyword+'&page='+page)
       return response.json()

#The information of the most popular movie list should be printed on the screen with the following information
    def Popilarity(self,page='1'):
        response=requests.get(self.api_url+'/3/movie/popular?api_key='+self.api_key+'&page='+page)
        return response.json()

#10 of the trending weekly movies should be printed on the screen, including the following information.
    def Trends(self):
        response=requests.get(self.api_url+'/3/trending/movie/week?api_key='+self.api_key)
        return response.json()

#According to vote_average, the list of the first 33 movies with the highest score should be printed on the screen with the following information
    def BestRated_33(self,page='1'):
        response=requests.get(self.api_url+'/3/movie/top_rated?api_key='+self.api_key+f'&page={page}')
        return response.json()

#In order to rate a movie we want, the necessary information should be obtained from the user and the rate given by the user should be post to the site via API.
    def Movie_Rating(self,movie_ID,rating):
        response=requests.post(self.api_url+'/3/movie/'+movie_ID+'/rating?api_key='+self.api_key+'&guest_session_id='+self.guest_session_ID,json={'value':rating})
        return response.json()


Result=TheMovieDb()
# print(Result.Trends())

#program menu.User makes choices via this.
while True:
    choice=input("""         
          WELCOME MOVIE ARCHIEVE
          $$$$$$$$$$$$$$$$$$$$$$

    You can make a selection from following options\n
    1-Search(with keywords)\n
    2-The most popular movie list\n
    3-The trending weekly 10 movies\n
    4-The list of the first 33 movies with the highest score\n
    5-Rate a movie\n
    Press any different from menu to exit\n
    -Make your choice from menu : """)

    Film_counter=1

    if choice=="1":
        keyword=input("Enter a keyword : ")
        result = Result.Search(keyword)
        total_page=result['total_pages']
        
        for page in range(1,total_page+1):
            result = Result.Search(keyword, str(page))
            
            for i in result['results']:
                
                print(f"\n Film {Film_counter}. \n    \nID: ", i['id'], "   \nName : " , i['original_title'])
                Film_counter+=1

    elif choice == "2":
        result = Result.Popilarity()
        total_page = 1

        for page in range(1, total_page+1):
            result = (Result.Popilarity(str(page)))
            for i in result['results'][:10]:
                print(f"""\nRank : {Film_counter} \nName :{i['original_title']} \npopularity : {i['popularity']} \nrelease date : {i['release_date']} \nvote average : {i['vote_average']} \n ---------""")
                Film_counter+=1

    elif choice=="3":
        result = Result.Trends()
        for i in result['results'][:10]:
            print(
                f"Name : {i['original_title']} \npopularity : {i['popularity']} \nrelease date : {i['release_date']} \nvote average : {i['vote_average']}\n ------------")
            Film_counter+=1

    elif choice == "4":
        # result = Result.BestRated_33()
        total_page=33//20+1
        for j in range(0,total_page):
            result=Result.BestRated_33(j+1)
            for i in result['results']:
                print(f"   Rank : {Film_counter} \nName :{i['original_title']} \npopularity : {i['popularity']} \nrelease date : {i['release_date']} \nvote average : {i['vote_average']}\n ------------")
                Film_counter+= 1
                if Film_counter == 34:
                        break

    elif choice=="5":
        print("Add a new movie \n")
        movie_ID=input("Enter Movie ID :")
        rating=(input("Rate this movie ( Values must be a multiple of 0.50,scale 0.5-10) : "))
        feedback=Result.Movie_Rating(movie_ID,rating)
        print(feedback["status_message"])

    else:
        break





















