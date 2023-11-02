def solution():
    mom_food_per_day = 1.5 * 3  # The mom foster dog eats 1.5 cups of food, three times per day
    puppy_food_per_day = 0.5 * 2 * 5  # The 5 puppies eat 0.5 cups of food twice per day
    total_food_per_day = mom_food_per_day + puppy_food_per_day  # Total food needed per day

    # Calculate the total food needed for 6 days
    total_food_needed = total_food_per_day * 6
    result = total_food_needed
    return result

print(solution())