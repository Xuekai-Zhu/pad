def solution():
    # Define the number of muffins Lana aims to sell and the number she has already sold
    total_goal = 20
    morning_sales = 12
    afternoon_sales = 4
    total_sales = morning_sales + afternoon_sales

    # Calculate the number of muffins Lana still needs to sell to hit her goal
    remaining_sales = total_goal - total_sales
    result = remaining_sales
    return result

print(solution())