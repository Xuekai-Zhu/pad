def solution():
    hours_run = 2
    calories_burnt_per_hour = 30
    additional_hours = 3

    # Calculate the total calories burnt in the initial 2-hour run
    initial_total_calories_burnt = hours_run * calories_burnt_per_hour

    # Calculate the total calories burnt if Jonah had run for 5 hours
    total_calories_burnt = (hours_run + additional_hours) * calories_burnt_per_hour

    # Calculate the additional calories burnt if Jonah had run for 5 hours
    additional_calories_burnt = total_calories_burnt - initial_total_calories_burnt

    result = additional_calories_burnt
    return result

print(solution())