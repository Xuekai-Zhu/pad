def solution():
    # Define the number of people and meals
    num_people = 6
    num_meals_per_day = 3

    # Calculate the total number of plates used per day
    plates_per_day = num_people * num_meals_per_day * 2

    # Calculate the total number of plates used for the 4 days
    plates_total = plates_per_day * 4

    result = plates_total
    return result

print(solution())