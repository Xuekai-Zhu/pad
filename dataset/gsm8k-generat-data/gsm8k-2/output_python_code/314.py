def solution():
    """There are enough provisions in a castle to feed 300 people for 90 days. After 30 days, 100 people leave the castle. How many more days are left until all the food runs out?"""
    total_people = 300
    total_days = 90
    remaining_days = total_days - 30
    remaining_people = total_people - 100
    food_per_person_per_day = 1 / total_people
    total_food = remaining_people * remaining_days * food_per_person_per_day
    result = total_food / (1 / remaining_people)
    return result

print(solution())