def solution():
    # Calculate the total amount of calories burnt by Jonah for 2 hours
    total_calories = 2 * 30  # Jonah burnt 30 calories every hour for 2 hours

    # Calculate the total amount of calories Jonah would have burnt for 5 hours
    total_calories_5hrs = 5 * 30

    # Calculate the difference in calories burnt between running for 2 hours and running for 5 hours
    calories_lost = total_calories_5hrs - total_calories
    result = calories_lost
    return result

print(solution())