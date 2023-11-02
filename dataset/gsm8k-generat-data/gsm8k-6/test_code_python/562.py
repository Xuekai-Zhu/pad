def solution():
    # Calculate the total amount of food needed for the mom dog and puppies for one day
    food_needed_per_day = 1.5 * 3 + (0.5 * 2 * 5) # mom dog eats 1.5 cups of food, three times a day and 5 puppies eat 0.5 cups of food, twice a day

    # Calculate the total amount of food needed for the next 6 days
    food_needed_for_six_days = 6 * food_needed_per_day

    result = food_needed_for_six_days
    return result

print(solution())