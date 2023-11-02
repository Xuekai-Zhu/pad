def solution():
    num_adults = 10
    adult_price = 8
    num_children = 11
    total_bill = 124

    # Calculate the total cost of all adult tickets
    adult_cost = num_adults * adult_price

    # Calculate the cost of all children's tickets
    children_cost = total_bill - adult_cost

    # Calculate the cost of one child's ticket
    child_price = children_cost / num_children
    result = child_price
    return result

print(solution())