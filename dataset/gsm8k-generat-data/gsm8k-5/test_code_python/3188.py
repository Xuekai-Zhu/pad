def solution():
    num_guests = 5  # Tom's parents and 3 siblings
    meals_per_day = 3  # Each person eats 3 times a day
    plates_per_meal = 2  # Each person uses 2 plates per meal
    days = 4  # Tom's family is staying for 4 days

    # Calculate the total number of plates used per day
    plates_per_day = num_guests * meals_per_day * plates_per_meal

    # Calculate the total number of plates used over the 4 days
    total_plates_used = plates_per_day * days

    result = total_plates_used
    return result

print(solution())