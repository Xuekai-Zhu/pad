def solution():
    # Calculate the number of strawberries Susan picks in each handful
    picked_per_handful = 4

    # Calculate the number of handfuls Susan needs to fill her basket
    num_handfuls = 60 / picked_per_handful

    # Calculate the total number of strawberries Susan picks
    total_picked = num_handfuls * 5

    # Return the result
    return total_picked

print(solution())