def solution():
    """Nine adults went to a play with seven children. Adult tickets are $11 each and children's tickets are $7 each. How many dollars more did the adults' tickets cost in total than the children's tickets in total?"""
    # Define the number of adults and children, and the prices of their tickets
    num_adults = 9
    num_children = 7
    adult_price = 11
    children_price = 7

    # Calculate the total cost of adult tickets and children's tickets
    adults_total = num_adults * adult_price
    children_total = num_children * children_price

    # Calculate the difference in cost between adult tickets and children's tickets
    cost_difference = adults_total - children_total

    # return the result
    result = cost_difference
    return result

print(solution())