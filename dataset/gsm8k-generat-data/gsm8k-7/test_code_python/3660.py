def solution():
    cone_price = 5
    expenses_percent = 0.8 # 80% expenses
    desired_profit = 200

    # Calculate the total sales needed to reach the desired profit
    total_sales = desired_profit / (1 - expenses_percent)

    # Calculate the number of ice cream cones needed to reach the total sales
    num_cones = total_sales / cone_price
    result = num_cones
    return result

print(solution())