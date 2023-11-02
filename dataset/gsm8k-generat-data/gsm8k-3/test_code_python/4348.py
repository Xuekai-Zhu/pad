def solution():
    """John buys 30 ducks for $10 each.  They weigh 4 pounds and he sells them for $5 per pound.  How much profit did he make?"""
    # Define the number of ducks purchased, the purchase price per duck, and the weight per duck
    num_ducks = 30
    purchase_price = 10
    weight_per_duck = 4

    # Calculate the total cost of the ducks
    total_cost = num_ducks * purchase_price

    # Calculate the total weight of the ducks
    total_weight = num_ducks * weight_per_duck

    # Calculate the total revenue from selling the ducks
    total_revenue = total_weight * 5

    # Calculate the profit from selling the ducks
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())