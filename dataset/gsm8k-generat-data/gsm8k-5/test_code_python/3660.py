def solution():
    cone_price = 5  # Marco sells each ice cream cone for $5
    expenses_ratio = 0.8  # Expenses are 80% of total sales for the day
    desired_profit = 200  # Marco wants to make a profit of $200 for the day

    # Calculate the total revenue needed to make the desired profit
    total_revenue = (desired_profit / (1 - expenses_ratio))

    # Calculate the number of cones Marco needs to sell to achieve the total revenue
    cones_sold = total_revenue / cone_price
    result = cones_sold
    return result

print(solution())