def solution():
    bag_cost = 3000
    profit_percentage = 0.15

    # Calculate the profit amount
    profit = bag_cost * profit_percentage

    # Calculate the selling price of the bag
    selling_price = bag_cost + profit
    result = selling_price
    return result

print(solution())