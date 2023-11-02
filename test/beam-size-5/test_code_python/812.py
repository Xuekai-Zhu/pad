def solution():
    num_goats = 3
    goat_price = 500

    num_cows = 2
    cow_price = 1500

    # Calculate the total cost of all goats
    total_goat_cost = num_goats * goat_price

    # Calculate the total cost of all cows
    total_cow_cost = num_cows * cow_price

    # Calculate the total cost of all items
    total_cost = total_goat_cost + total_cow_cost
    result = total_cost
    return result

print(solution())