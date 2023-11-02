def solution():
    num_adults = 2 # Two adults (her mom and dad)
    adult_price = 12

    num_children = 4 # Three little sisters and one grandma
    child_price = 10

    # Calculate the total cost for all adults
    total_adult_cost = num_adults * adult_price

    # Calculate the total cost for all children
    total_child_cost = num_children * child_price

    # Calculate the total cost for all tickets
    total_cost = total_adult_cost + total_child_cost
    result = total_cost
    return result

print(solution())