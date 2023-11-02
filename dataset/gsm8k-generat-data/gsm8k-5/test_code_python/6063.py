def solution():
    time_available = 2*60  # Megan has 2 hours (120 minutes) to prepare the dishes
    time_per_dish = 20  # It takes 20 minutes to prepare one dish
    dishes_prepared = time_available // time_per_dish  # Calculate number of dishes Megan can prepare

    # Calculate the total number of people Megan can feed with the dishes she prepared
    people_fed = dishes_prepared * 5
    result = people_fed
    return result

print(solution())