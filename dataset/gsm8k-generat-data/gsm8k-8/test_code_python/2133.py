def solution():
    total_cost = 827
    price_difference = 127
    
    # Set up a system of equations:
    # x + y = total_cost
    # x - y = price_difference
    # Solve for x (the price of the first commodity)
    x = (total_cost + price_difference) / 2
    
    result = x
    return result

print(solution())