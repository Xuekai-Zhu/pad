def solution():
    
    dish_time = 20
    dishes_per_hour = 60 / dish_time
    dishes_prepared = 2 * dishes_per_hour
    people_fed = dishes_prepared * 5
    result = people_fed
    return result

print(solution())