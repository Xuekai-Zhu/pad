def solution():
    manicure_cost = 30  # The manicure cost $30
    tip_percent = 30  # Tim tips the beautician 30% of the manicure cost

    # Calculate the total cost, including the tip
    total_cost = manicure_cost + (manicure_cost * (tip_percent/100))
    result = total_cost
    return result

print(solution())