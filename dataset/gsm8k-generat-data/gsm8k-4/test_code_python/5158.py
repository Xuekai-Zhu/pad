def solution():
    """Dalton, Hunter, and Alex started a Superhero Fan Club. They set a goal to watch as many Superhero movies as they could in one summer. Dalton watched 7 movies, Hunter watched 12, and Alex watched 15. They all watched 2 movies together, but every other movie they watched was different. How many different movies did they see?"""
    
    # Find the total number of movies watched by all three of them
    total_movies = Dalton + Hunter + Alex - 2*3
    
    result = total_movies
    return result

print(solution())