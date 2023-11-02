def solution():
    # Calculate the calorie deficit per day
    calorie_deficit = 2300 - 1800

    # Calculate the calorie deficit per pound of weight loss
    calorie_deficit_per_pound = 4000

    # Calculate the calorie deficit needed to lose 10 pounds
    calorie_deficit_for_10_pounds = 10 * calorie_deficit_per_pound

    # Calculate the number of days needed to achieve the calorie deficit for 10 pounds of weight loss
    days_to_lose_10_pounds = calorie_deficit_for_10_pounds / calorie_deficit

    result = days_to_lose_10_pounds
    return result

print(solution())