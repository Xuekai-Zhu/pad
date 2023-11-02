def solution():
    goal = 20  # Lana aims to sell 20 muffins
    morning_sales = 12  # Lana sells 12 muffins in the morning
    afternoon_sales = 4  # Lana sells 4 muffins in the afternoon

    # Calculate the number of muffins Lana still needs to sell to hit her goal
    remaining_sales = goal - morning_sales - afternoon_sales
    result = remaining_sales
    return result

print(solution())