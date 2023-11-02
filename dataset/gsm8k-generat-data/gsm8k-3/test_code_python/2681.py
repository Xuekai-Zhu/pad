def solution():
    """Jonathan eats 2500 calories every day except for Saturday, when he consumes an extra 1000 calories.  He burns 3000 calories every day.  What is his weekly caloric deficit?"""
    # Define the number of calories Jonathan eats each day and the number of calories he burns each day
    DAILY_CALORIES_EATEN = 2500
    SATURDAY_CALORIES_EATEN = 3500
    DAILY_CALORIES_BURNED = 3000

    # Calculate the total number of calories Jonathan eats during a week
    weekly_calories_eaten = (6 * DAILY_CALORIES_EATEN) + SATURDAY_CALORIES_EATEN

    # Calculate the total number of calories Jonathan burns during a week
    weekly_calories_burned = 7 * DAILY_CALORIES_BURNED

    # Calculate Jonathan's weekly caloric deficit
    weekly_caloric_deficit = weekly_calories_burned - weekly_calories_eaten

    # Display Jonathan's weekly caloric deficit
    result = weekly_caloric_deficit
    return result

print(solution())