def solution():
    """Janet filmed a new movie that is 60% longer than her previous 2-hour long movie. Her previous movie cost $50 per minute to film, and the newest movie cost twice as much per minute to film as the previous movie. What was the total amount of money required to film Janet's entire newest film?"""
    previous_movie_length = 120 #in minutes
    new_movie_length = previous_movie_length * 1.6
    previous_movie_cost_per_minute = 50 #in dollars
    new_movie_cost_per_minute = previous_movie_cost_per_minute * 2
    total_cost = (previous_movie_length * previous_movie_cost_per_minute) + (new_movie_length * new_movie_cost_per_minute)
    result = total_cost
    return result

print(solution())