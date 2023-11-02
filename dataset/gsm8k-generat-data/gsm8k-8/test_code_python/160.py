def solution():
    # Calculate the cost of the burgers
    burger_cost = 100 * 3

    # Calculate the total cost of everything
    total_cost = burger_cost + 80 + 200

    # Split the cost among four people
    split_cost = total_cost / 4

    # John pays for his share and the alcohol
    john_cost = split_cost + 200

    result = john_cost
    return result

print(solution())