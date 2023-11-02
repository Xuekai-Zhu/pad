def solution():
    num_pumpkin_pies = 10
    pumpkin_pie_cost = 3

    num_cherry_pies = 12
    cherry_pie_cost = 5

    desired_profit = 20

    # Calculate the total cost of making all pumpkin pies
    total_pumpkin_cost = num_pumpkin_pies * pumpkin_pie_cost

    # Calculate the total cost of making all cherry pies
    total_cherry_cost = num_cherry_pies * cherry_pie_cost

    # Calculate the total cost of making all pies
    total_cost = total_pumpkin_cost + total_cherry_cost

    # Calculate the price per pie to make the desired profit
    num_total_pies = num_pumpkin_pies + num_cherry_pies
    price_per_pie = (total_cost + desired_profit) / num_total_pies
    result = price_per_pie
    return result

print(solution())