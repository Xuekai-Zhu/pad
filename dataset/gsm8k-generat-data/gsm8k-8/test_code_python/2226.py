def solution():
    # Define the initial amount of sugar used in the first week
    sugar = 24

    # Calculate the amount of sugar used in the fourth week, which is half the amount used in the third week
    sugar_fourth_week = sugar / 2 / 2 / 2

    result = sugar_fourth_week
    return result

print(solution())