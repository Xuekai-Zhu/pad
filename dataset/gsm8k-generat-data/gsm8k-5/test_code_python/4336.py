def solution():
    calories_per_hour = 30  # Jonah burns 30 calories per hour
    hours_run = 2  # Jonah runs for 2 hours

    # Calculate the total calories burnt in 2 hours
    total_calories = calories_per_hour * hours_run

    # Calculate the additional calories Jonah would have burnt if he ran for 5 hours
    additional_hours = 5 - hours_run
    additional_calories = additional_hours * calories_per_hour

    # Calculate the total calories Jonah would have burnt in 5 hours
    total_calories_5_hours = total_calories + additional_calories

    # Calculate the difference in calories burnt between running for 2 hours and running for 5 hours
    difference_in_calories = total_calories_5_hours - total_calories
    result = difference_in_calories
    return result

print(solution())