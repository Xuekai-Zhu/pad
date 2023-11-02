def solution():
    soda_cost = 1  # Each soda costs $1
    soup_cost = 3 * soda_cost  # Each soup costs as much as the 3 combined sodas
    sandwich_cost = 9 * soda_cost  # The sandwich costs 3 times as much as the soup

    # Calculate the total cost of the order
    total_cost = (3 * soda_cost) + (2 * soup_cost) + sandwich_cost
    result = total_cost
    return result

print(solution())