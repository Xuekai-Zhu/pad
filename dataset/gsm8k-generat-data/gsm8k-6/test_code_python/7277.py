def solution():
    # Calculate the cost of one jersey
    jersey_cost = 560/4  # jerseys cost 1/4 price of one pair of shoes
    # Calculate the total cost of 6 pairs of shoes
    shoe_cost = (560 - jersey_cost*4)/6  # Total cost - cost of jerseys = cost of shoes, divided by 6 to get cost of one shoe
    result = shoe_cost*6  # Multiply cost of one shoe by 6 to get the total cost of 6 pairs of shoes
    return result

print(solution())