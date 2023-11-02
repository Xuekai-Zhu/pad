def solution():
    # Convert preparation time to minutes and calculate total preparation time
    preparation_time = 2 * 60
    dish_prep_time = 20
    total_dish_count = preparation_time // dish_prep_time

    # Calculate the total number of people the dishes can feed
    people_per_dish = 5
    total_people_count = total_dish_count * people_per_dish
    result = total_people_count
    return result

print(solution())