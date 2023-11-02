def solution():
    # Calculate the total calories in 10 burritos
    burrito_calories = 10 * 120

    # Calculate the calories per dollar for the burritos
    burrito_cal_per_dollar = burrito_calories / 6

    # Calculate the total calories in 5 burgers
    burger_calories = 5 * 400

    # Calculate the calories per dollar for the burgers
    burger_cal_per_dollar = burger_calories / 8

    # Calculate the difference in calories per dollar between the two options
    difference = burger_cal_per_dollar - burrito_cal_per_dollar
    result = difference
    return result

print(solution())