import requests


class Themovie:
    def __init__(self):
        self.url = "https://api.themoviedb.org/3"
        self.apikey = "*****************"
        self.guest_session_id = requests.get(
            "https://api.themoviedb.org/3/authentication/guest_session/new?api_key="+self.apikey).json()['guest_session_id']

    def search(self, keyword, page=1):
        params = {"query": keyword,
                  "api_key": self.apikey,
                  "page": page}
        searchurl = "/search/movie"
        result = requests.get(self.url+searchurl, params=params)
        return result.json()

    def populermovies(self, page=1):
        url = "/movie/popular"
        params = {"api_key": self.apikey,
                  "page": page}
        result = requests.get(self.url+url, params=params)
        return result.json()

    def weeklytrend(self):
        url = "/trending/movie/week"
        params = {"api_key": self.apikey}
        result = requests.get(self.url+url, params=params)
        return result.json()

    def toprated(self, page=1):
        url = "/movie/top_rated"
        params = {"api_key": self.apikey,
                  "page": page}
        result = requests.get(self.url+url, params=params)
        return result.json()

    def voterate(self, movieid, vote):
        url = f"/movie/{movieid}/rating"
        params = {"api_key": self.apikey,
                  "guest_session_id": self.guest_session_id}
        result = requests.post(
            self.url+url, params=params, json={"value": vote})
        return result.json()


movie_api = Themovie()

while True:

    choice = input("1-Searching movies according to keyword\n2-Most popular films\n3-10 of trending weekly movies\n4-First highest score 33 films.\n5-Rate a movie\n-Press any button for exit\nChoice :  ")
    if choice == "1":
        keyword = input("Enter a keyword : ")
        result = movie_api.search(keyword)
        total_page = result['total_pages']

        for page in range(1, total_page+1):
            result = movie_api.search(keyword, page)
            for results in result['results']:
                print("id: ", results['id'], "Name : ",
                      results['original_title'])
            nextpage = input(
                "press 'm' if you want to see next page\npress any key to go upper menu ")
            if nextpage == "m" or nextpage == "M":
                pass
            else:
                break
    elif choice == "2":
        result = movie_api.populermovies()
        total_page = result['total_pages']
        for page in range(1, total_page+1):
            result = (movie_api.populermovies(page))
            for results in result['results']:
                print(
                    f"Name :{results['original_title']} popularity : {results['popularity']} release date  {results['release_date']} vote average : {results['vote_average']}")
            nextpage = input(
                "press 'm' if you want to see next page\npress any key to go upper menu ")
            if nextpage == "m" or nextpage == "M":
                pass
            else:
                break
    elif choice == "3":
        counter = 11
        result = movie_api.weeklytrend()
        for results in result['results']:
            counter -= 1
            if counter == 0:
                break
            print(
                f"Name :{results['original_title']} popularity : {results['popularity']} release date  {results['release_date']} vote average : {results['vote_average']}")
        print(
            "*******************************************************************************")
    elif choice == "4":
        result = movie_api.toprated()
        counter = 0
        for results in result['results']:
            counter += 1
            print(
                f"Name :{results['original_title']} popularity : {results['popularity']} release date  {results['release_date']} vote average : {results['vote_average']}")
            if counter == 20:
                for results in result['results'][:13]:
                    result = movie_api.toprated(2)
                    print(
                        f"Name :{results['original_title']} popularity : {results['popularity']} release date  {results['release_date']} vote average : {results['vote_average']}")
    elif choice == "5":
        movieid = int(input("Enter Movie Id : "))
        vote = float(input("Your Rate out of 10 : "))
        result = movie_api.voterate(movieid, vote)
        print(result['status_message'])

    else:
        break
