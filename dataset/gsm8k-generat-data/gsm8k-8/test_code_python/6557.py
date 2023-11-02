def solution():
    # Define the number of bass caught
    bass = 32

    # Calculate the number of trout caught (1/4 as many as bass)
    trout = 0.25 * bass

    # Calculate the number of blue gill caught (double the bass)
    blue_gill = 2 * bass

    # Calculate the total number of fish caught
    total_fish = bass + trout + blue_gill
    result = total_fish
    return result

print(solution())