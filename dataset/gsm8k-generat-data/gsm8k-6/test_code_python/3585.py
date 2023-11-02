def solution():
    # Calculate the total number of meals available
    total_meals = 113 + 50  # 50 extra meals provided by Sole Mart

    # Calculate the number of meals left to distribute
    meals_left = total_meals - 85  # 85 meals already given away
    result = meals_left
    return result

print(solution())