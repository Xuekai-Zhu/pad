def solution():
    # Price for adult tickets
    adult_price = 22

    # Price for children tickets
    children_price = 7

    # Total number of adults and children in the family
    num_adults = 2
    num_children = 2

    # Total cost of tickets for the family
    total_cost = adult_price * num_adults + children_price * num_children
    result = total_cost
    return result

print(solution())