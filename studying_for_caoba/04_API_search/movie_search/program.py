import api

def main():
    # it is better if user put word
    keyword = input("Keyword of title search: ")
    results = api.find_movie_by_title(keyword)
    print(f"There are {len(results)} movies found.") 

    for r in results:
        #print(f"Title: {r.get('title')}") # Before using list of Movies
        print(f"Title: {r.title} has score {r.imdb_score}")
    

if '__main__' == __name__:
    main()
