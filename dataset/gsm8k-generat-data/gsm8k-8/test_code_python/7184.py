def solution():
    # Define the cost and selling price of each pair of sunglasses
    cost_per_pair = x
    selling_price_per_pair = 30

    # Calculate the total cost of the sunglasses
    total_cost = cost_per_pair * 10

    # Calculate the total revenue from selling the sunglasses
    total_revenue = selling_price_per_pair * 10

    # Calculate the profit from selling the sunglasses
    profit = total_revenue - total_cost

    # Calculate the amount spent on the new sign
    sign_cost = 20

    # Calculate the amount left after buying the sign
    left_money = profit / 2 - sign_cost

    # Calculate the cost per pair of sunglasses
    cost_per_pair = total_cost / 10

    result = cost_per_pair
    return result

print(solution())