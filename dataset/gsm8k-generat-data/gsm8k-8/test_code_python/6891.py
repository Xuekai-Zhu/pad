def solution():
    # Calculate the total number of fish caught
    total_fish = 4 + 1 + 3 + 2 + 5

    # Calculate the total number of fish after throwing back the small ones
    total_good_fish = total_fish - 3

    # Calculate the total number of fish filets
    total_filets = 2 * total_good_fish
    result = total_filets
    return result

print(solution())