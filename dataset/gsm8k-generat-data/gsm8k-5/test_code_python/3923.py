def solution():
    apple_price = 1.25  # Reginald sells each apple for $1.25
    bike_cost = 80  # Reginald's bike cost $80
    repair_cost = bike_cost * 0.25  # The repair cost is 25% of the bike cost
    total_cost = bike_cost + repair_cost  # The total cost is the sum of the bike cost and repair cost

    # Calculate the total revenue from selling apples
    total_revenue = total_cost / (1/5)  # 1/5 of the money remains after the repairs are paid for
    total_apples = total_revenue / apple_price  # Calculate the total number of apples sold

    result = total_apples
    return result

print(solution())