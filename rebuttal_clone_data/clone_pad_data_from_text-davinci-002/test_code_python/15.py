def solution():
    """James creates a media empire. He creates a movie for $2000. Each DVD cost $6 to make. He sells it for 2.5 times that much.  He sells 500 movies a day for 5 days a week. How much profit does he make in 20 weeks?"""
    
    cost_to_make_movie = 2000
    cost_to_make_dvd = 6
    price_per_movie = cost_to_make_movie * 2.5
    movies_sold_per_day = 500
    days_per_week = 5
    movies_sold_per_week = movies_sold_per_day * days_per_week
    weeks = 20
    movies_sold_in_20_weeks = movies_sold_per_week * weeks
    profit = movies_sold_in_20_weeks * (price_per_movie - cost_to_make_dvd)
    
    result = profit
    return result

print(solution())