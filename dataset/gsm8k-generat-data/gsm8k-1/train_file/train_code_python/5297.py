def solution():
    """Carla works at a food bank and she currently has stocked up 2000 cans of food. One day, 500 people showed up and took 1 can of food each. Carla had to then restock 1500 more cans to keep up with demand. The next day, 1000 people showed up and took 2 cans of food each. Carla restocked again with 3000 cans of food this time. How many cans of food did Carla give away?"""
    initial_stock = 2000
    first_day_people = 500
    first_day_consumption = first_day_people * 1
    restock_one = 1500
    second_day_people = 1000
    second_day_consumption = second_day_people * 2
    restock_two = 3000
    total_consumption = first_day_consumption + second_day_consumption
    total_stock = initial_stock + restock_one + restock_two
    total_given_away = total_consumption - (total_stock - initial_stock)
    
    return total_given_away

print(solution())