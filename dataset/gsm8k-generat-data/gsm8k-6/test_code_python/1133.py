def solution():
    # Calculate the total amount of water needed in ounces
    total_water = 100 * 3  # Each balloon holds 3 ounces of water

    # Calculate the number of bottles of water needed and the cost
    num_bottles = total_water // 50 + (1 if total_water % 50 != 0 else 0)  # Round up to the nearest bottle
    cost = num_bottles * 2.5  # Each bottle costs $2.5

    # Calculate the amount of change Marcus will have
    change = 20 - cost
    result = change
    return result

print(solution())