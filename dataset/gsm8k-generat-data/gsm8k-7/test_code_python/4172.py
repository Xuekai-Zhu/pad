def solution():
    num_adults = 9
    adult_price = 11

    num_children = 7
    child_price = 7

    # Calculate the total cost of all adult tickets
    total_adult_cost = num_adults * adult_price

    # Calculate the total cost of all children's tickets
    total_child_cost = num_children * child_price

    # Calculate the difference in cost between adult and children's tickets
    difference = total_adult_cost - total_child_cost
    result = difference
    return result

print(solution())