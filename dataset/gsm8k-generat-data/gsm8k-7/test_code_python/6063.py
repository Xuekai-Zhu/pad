def solution():
    prep_time_per_dish = 20 # in minutes
    dishes_per_hour = 60 / prep_time_per_dish # dishes Megan can prepare in an hour
    dishes_prepared = dishes_per_hour * 2 # total dishes she prepares in 2 hours

    servings_per_dish = 5
    total_servings = dishes_prepared * servings_per_dish
    result = total_servings
    return result

print(solution())