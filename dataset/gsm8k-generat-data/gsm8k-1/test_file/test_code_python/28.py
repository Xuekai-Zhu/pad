def solution():
    """John takes care of 10 dogs. Each dog takes .5 hours a day to walk and take care of their business. How many hours a week does he spend taking care of dogs?"""
    dogs = 10
    hours_per_day_per_dog = 0.5
    days_per_week = 7
    total_hours = dogs * hours_per_day_per_dog * days_per_week
    result = total_hours
    return result

print(solution())