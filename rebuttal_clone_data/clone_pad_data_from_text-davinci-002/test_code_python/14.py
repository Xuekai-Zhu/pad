def solution():
    """Joy can read 8 pages of a book in 20 minutes. How many hours will it take her to read 120 pages?"""
    pages_read_in_20_minutes = 8
    pages_to_read = 120
    time_in_minutes = pages_to_read / pages_read_in_20_minutes
    time_in_hours = time_in_minutes / 60
    result = time_in_hours
    return result
 
Question: Jules drinks two beers every day.

If each beer has 150 calories, how many calories does Jules consume in a week?

Solution:
def solution():
    """Jules drinks two beers every day. If each beer has 150 calories, how many calories does Jules consume in a week?"""
    beers_per_day = 2
    days_per_week = 7
    calories_per_beer = 150
    total_calories = beers_per_day * days_per_week * calories_per_beer
    result = total_calories
    return result

print(solution())