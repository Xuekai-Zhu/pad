def solution():
    """Carla works at a food bank and she currently has stocked up 2000 cans of food. One day, 500 people showed up and took 1 can of food each. Carla had to then restock 1500 more cans to keep up with demand. The next day, 1000 people showed up and took 2 cans of food each. Carla restocked again with 3000 cans of food this time. How many cans of food did Carla give away?"""
    starting_cans = 2000
    first_day_people = 500
    first_day_cans = 500
    restock_1 = 1500
    second_day_people = 1000
    second_day_cans = 2000
    restock_2 = 3000
    total_given_away = first_day_cans + (second_day_people * 2)
    result = total_given_away
    return result

print(solution())