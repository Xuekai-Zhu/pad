def solution():
    recommended_daily_vegetable_intake = 2
    num_days_so_far = 5
    total_vegetables_eaten_so_far = 8

    # Calculate the total number of vegetables Sarah would need to have eaten by the end of the week
    total_vegetables_for_week = recommended_daily_vegetable_intake * 7

    # Subtract the vegetables Sarah has already eaten from the total for the week to determine how many more she needs to eat
    vegetables_left_to_eat = total_vegetables_for_week - total_vegetables_eaten_so_far

    # Divide the number of vegetables left to eat by the number of days left in the week to determine how many Sarah needs to eat per day for the rest of the week.
    days_left_in_week = 7 - num_days_so_far
    daily_vegetable_intake_needed = vegetables_left_to_eat / days_left_in_week

    result = daily_vegetable_intake_needed
    return result

print(solution())