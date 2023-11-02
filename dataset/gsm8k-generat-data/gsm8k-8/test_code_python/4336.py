def solution():
    # Define the number of hours Jonah runs for originally and wants to run for
    original_hours = 2
    new_hours = 5

    # Define the number of calories Jonah burns per hour
    calorie_burn_per_hour = 30

    # Calculate the total calories Jonah burns initially and would have burned if he ran for the new time
    original_calories_burned = original_hours * calorie_burn_per_hour
    new_calories_burned = new_hours * calorie_burn_per_hour

    # Calculate the difference in calories burned
    additional_calories_burned = new_calories_burned - original_calories_burned
    result = additional_calories_burned
    return result

print(solution())