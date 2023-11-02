def solution():
    # Calculate the total number of fish in all the bowls except for the table with 3 fish
    total_fish = 2 * (32 - 1)

    # Add the 3 fish from the special table
    total_fish += 3

    result = total_fish
    return result

print(solution())