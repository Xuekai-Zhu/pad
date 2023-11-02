def solution():
    num_people_initial = 300
    num_days_initial = 90
    num_people_remaining = 200
    num_days_elapsed = 30

    # Calculate the total amount of food available initially
    total_food_initial = num_people_initial * num_days_initial

    # Calculate the amount of food consumed after 30 days
    total_food_consumed = num_people_initial * num_days_elapsed

    # Calculate the amount of food remaining after 30 days
    total_food_remaining = total_food_initial - total_food_consumed

    # Calculate the number of days it will take to run out of food with the remaining people
    days_remaining = total_food_remaining / (num_people_remaining * 1.0)
    result = days_remaining
    return result

print(solution())