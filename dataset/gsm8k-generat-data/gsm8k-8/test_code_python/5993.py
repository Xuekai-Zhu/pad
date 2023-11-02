def solution():
    # Calculate the daily calorie deficit
    calorie_deficit = 2300 - 1800
    # Calculate the number of calories needed to burn to lose 1 pound
    calories_per_pound = 4000
    # Calculate the number of days needed to lose 1 pound
    days_per_pound = calories_per_pound / calorie_deficit
    # Calculate the number of days needed to lose 10 pounds
    days_to_lose_10_pounds = days_per_pound * 10
    result = days_to_lose_10_pounds
    return result

print(solution())