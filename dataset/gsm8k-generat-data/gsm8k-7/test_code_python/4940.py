def solution():
    # Let x be the regular price of one pen
    x = 0

    # Calculate the cost of the first 10 pens at regular price
    cost_first_10 = 10 * x

    # Calculate the cost of the next 10 pens at half off
    cost_next_10 = 10 * (x / 2)

    # Calculate the total cost of all 20 pens
    total_cost = cost_first_10 + cost_next_10

    # Since we know the total cost is $30, we can solve for x
    x = total_cost / 20

    result = x
    return result

print(solution())