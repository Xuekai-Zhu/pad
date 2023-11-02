def solution():
    # Calculate total calories consumed from Cheezits
    total_cheezit_calories = 3 * 2 * 150

    # Calculate calories burned during the run
    calories_burned = 40 * 12

    # Calculate the net calorie intake
    net_calorie_intake = total_cheezit_calories - calories_burned

    # Check if calorie intake was a surplus
    if net_calorie_intake > 0:
        excess_calories = net_calorie_intake
    else:
        excess_calories = 0

    result = excess_calories
    return result

print(solution())