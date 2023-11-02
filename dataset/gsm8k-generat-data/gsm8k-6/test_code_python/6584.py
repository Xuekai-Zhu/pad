def solution():
    # Calculate the cost of each item after discount
    tshirt_cost = 20 * 0.9
    pants_cost = 80 * 0.9
    shoes_cost = 150 * 0.9

    # Calculate the total cost of all items
    total_cost = 4 * tshirt_cost + 3 * pants_cost + 2 * shoes_cost

    result = total_cost
    return result

print(solution())