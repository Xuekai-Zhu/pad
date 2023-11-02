def solution():
    # Calculate the daily calorie deficit (calories burned - calories consumed)
    daily_calorie_deficit = 2500 - 2000

    # Calculate the calorie deficit in 5 pounds of body fat
    calorie_deficit_5_pounds = 5 * 3500

    # Calculate the number of days it will take to burn off 5 pounds at the daily calorie deficit
    days_to_burn_off_5_pounds = calorie_deficit_5_pounds / daily_calorie_deficit
    result = days_to_burn_off_5_pounds
    return result

print(solution())