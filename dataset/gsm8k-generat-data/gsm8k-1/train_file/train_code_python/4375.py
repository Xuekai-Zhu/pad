def solution():
    """Austin receives $5 for every hour he helps his father build a deck in their backyard. He works for 2 hours on Mondays, an hour on Wednesdays, and 3 hours on Fridays. If Austin wants to buy a bicycle that costs $180, how many weeks does he have to work?"""
    monday_hours = 2
    wednesday_hours = 1
    friday_hours = 3
    total_hours = monday_hours + wednesday_hours + friday_hours
    weekly_earnings = total_hours * 5
    bike_cost = 180
    weeks_to_work = bike_cost / weekly_earnings
    result = weeks_to_work
    return result

print(solution())