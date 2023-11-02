def solution():
    """Jon runs a website where he gets paid for every person who visits. He gets paid $0.10 for every person who visits. Each hour he gets 50 visits. His website operates 24 hours a day. How many dollars does he make in a 30 day month?"""
    visits_per_hour = 50
    hours_per_day = 24
    days_per_month = 30
    dollars_per_visit = 0.1
    total_visits = visits_per_hour * hours_per_day * days_per_month
    dollars_made = total_visits * dollars_per_visit
    result = dollars_made
    return result

print(solution())