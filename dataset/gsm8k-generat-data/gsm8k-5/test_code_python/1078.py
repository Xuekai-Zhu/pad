def solution():
    # Calculate the total number of fish in the fishbowls
    total_fish = (32 - 1) * 2  # 32 tables minus the one table with 3 fish, times 2 fish per bowl

    # Add the 3 fish from the one table to the total
    total_fish += 3

    result = total_fish
    return result

print(solution())