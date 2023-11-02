def solution():
    # Calculate the total number of ball bearings needed
    total_bearings = 10 * 30  # 10 machines and 30 ball bearings each

    # Calculate the total cost without sale or discount
    total_cost = total_bearings * 1  # $1 per ball bearing

    # Calculate the total cost with sale but no discount
    sale_cost = total_bearings * 0.75  # $.75 per ball bearing

    # Calculate the total cost with sale and discount
    discount_cost = sale_cost * 0.8  # 20% discount

    # Calculate the amount saved by buying during the sale
    savings = total_cost - discount_cost

    result = savings
    return result

print(solution())