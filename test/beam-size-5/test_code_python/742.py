def solution():
    num_adults = 2
    adult_fee = 26

    num_children = 2
    child_fee = 12

    # Calculate the total cost of the first amusement park
    first_cost = (num_adults * adult_fee) + (num_children * child_fee)

    # Calculate the total cost of the second amusement park
    second_cost = (num_adults * adult_fee) + (num_children * child_fee)

    # Calculate the amount saved by choose the second amusement park
    savings = second_cost - first_cost
    result = savings
    return result

print(solution())