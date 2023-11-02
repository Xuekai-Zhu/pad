def solution():
    """There are enough provisions in a castle to feed 300 people for 90 days. After 30 days, 100 people leave the castle. How many more days are left until all the food runs out?"""
    people_initially = 300
    days_initially = 90
    days_elapsed = 30
    people_remaining = 300 - 100
    food_consumption_rate = people_initially * days_initially
    remaining_food = food_consumption_rate - (people_remaining * (days_initially - days_elapsed))
    days_remaining = remaining_food / (people_remaining * days_initially)
    result = days_remaining
    return result

print(solution())