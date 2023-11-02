def solution():
    num_bags = 3
    ounces_per_bag = 2
    calories_per_ounce = 150
    minutes_exercised = 40
    calories_burned_per_minute = 12

    # Calculate the total number of ounces of Cheezits eaten
    total_ounces = num_bags * ounces_per_bag

    # Calculate the total number of calories consumed
    total_calories_consumed = total_ounces * calories_per_ounce

    # Calculate the number of calories burned during the run
    calories_burned_during_run = minutes_exercised * calories_burned_per_minute

    # Calculate the excess calories consumed
    excess_calories_consumed = total_calories_consumed - calories_burned_during_run

    result = excess_calories_consumed
    return result

print(solution())