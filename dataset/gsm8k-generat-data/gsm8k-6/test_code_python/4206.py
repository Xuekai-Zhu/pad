def solution():
    # Calculate the total amount of special dog food needed in ounces
    special_food_needed = 2*60 + 4*(365-60)  # puppy needs 2 oz of food per day for 60 days, and 4 oz per day for the rest of the year

    # Convert ounces to pounds
    special_food_needed_pounds = special_food_needed / 16

    # Calculate the number of bags needed
    bags_needed = special_food_needed_pounds / 5

    result = bags_needed
    return result

print(solution())