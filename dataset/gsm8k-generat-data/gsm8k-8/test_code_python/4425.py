def solution():
    # Define the fraction of a bottle she drinks every night and the cost per bottle
    fraction_drunk = 1/5
    bottle_cost = 2.0

    # Calculate the amount she drinks in a year (365 nights) and the total cost
    total_drunk = fraction_drunk * 365
    total_cost = total_drunk * bottle_cost
    result = total_cost
    return result

print(solution())