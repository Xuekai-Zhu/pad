def solution():
    """Joy fosters dogs.  The mom foster dog eats 1.5 cups of food, three times a day.  The puppies each eat 1/2 cup of food, twice a day.  There are 5 puppies.  How much food will Joy need for the next 6 days?"""
    # Calculate the total amount of food needed for the mom dog for 6 days
    mom_food_per_day = 1.5 * 3
    mom_food_for_six_days = mom_food_per_day * 6

    # Calculate the total amount of food needed for the puppies for 6 days
    puppy_food_per_day = 0.5 * 2 * 5
    puppy_food_for_six_days = puppy_food_per_day * 6

    # Calculate the total amount of food needed for all the dogs for 6 days
    total_food_for_six_days = mom_food_for_six_days + puppy_food_for_six_days

    # Display the total amount of food needed for 6 days
    result = total_food_for_six_days
    return result

print(solution())