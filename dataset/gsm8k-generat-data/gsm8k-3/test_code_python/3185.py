def solution():
    """Gordon owns 3 restaurants, his first restaurant serves 20 meals, his second restaurant serves 40 meals, and his third restaurant serves 50 meals per day. How many meals do his 3 restaurants serve per week?"""
    # Define the number of meals served at each restaurant per day
    RESTAURANT_1_MEALS = 20
    RESTAURANT_2_MEALS = 40
    RESTAURANT_3_MEALS = 50

    # Define the number of days in a week
    DAYS_IN_WEEK = 7

    # Calculate the total number of meals served per week
    total_meals = (RESTAURANT_1_MEALS + RESTAURANT_2_MEALS + RESTAURANT_3_MEALS) * DAYS_IN_WEEK

    # Display the total number of meals served per week
    result = total_meals
    return result

print(solution())