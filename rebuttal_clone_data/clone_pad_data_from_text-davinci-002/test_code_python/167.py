def solution():
    """Janet filmed a new movie that is 60% longer than her previous 2-hour long movie. Her previous movie cost $50 per minute to film, and the newest movie cost twice as much per minute to film as the previous movie. What was the total amount of money required to film Janet's entire newest film?"""
    old_movie_length = 2 * 60
    new_movie_length = old_movie_length * 1.6
    old_movie_cost_per_minute = 50
    new_movie_cost_per_minute = old_movie_cost_per_minute * 2
    total_cost = new_movie_length * new_movie_cost_per_minute
    result = total_cost
    
    return result

print(solution())