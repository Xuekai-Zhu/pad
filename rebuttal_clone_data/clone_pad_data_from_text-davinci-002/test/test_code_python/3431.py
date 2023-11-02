def solution():
    minutes_per_dish = 20
    minutes_per_hour = 60
    hours_available = 2
    dishes_per_hour = minutes_per_hour / minutes_per_dish
    total_dishes = dishes_per_hour * hours_available
    people_per_dish = 5
    total_people = total_dishes * people_per_dish
    result = total_people
    return result

print(solution())