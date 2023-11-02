def solution():
    pumpkin_cost = 3  # Cost to make each pumpkin pie is $3
    cherry_cost = 5  # Cost to make each cherry pie is $5
    total_cost = (10 * pumpkin_cost) + (12 * cherry_cost)  # Total cost to make all the pies
    total_revenue = total_cost + 20  # Benny wants to make a profit of $20 selling all the pies

    # Calculate the price per pie
    price_per_pie = total_revenue / 22  # Benny is making 10 pumpkin and 12 cherry pies
    result = price_per_pie
    return result

print(solution())