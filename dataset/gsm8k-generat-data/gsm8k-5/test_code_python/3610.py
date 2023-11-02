def solution():
    # Calculate the cost of soda and chicken wings that Elle and Andrea will share
    soda_cost = 4 * 1.5  # Each can of soda costs $1.5 and they are buying 4 cans in total
    wings_cost = 10

    # Calculate the total cost of the party
    total_cost = 20 + 2 + soda_cost + wings_cost + 5

    # Calculate the cost of the party minus Mary's contribution
    rest_cost = total_cost - 20 - 2

    # Calculate the difference in cost
    difference = (20 + 2) - rest_cost
    result = difference
    return result

print(solution())