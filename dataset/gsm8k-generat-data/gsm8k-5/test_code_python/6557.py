def solution():
    bass = 32  # There are 32 bass
    trout = bass / 4  # There are 1/4 as many trout as bass
    blue_gill = 2 * bass  # There are double the number of blue gill as bass

    # Calculate the total number of fish caught
    total_fish = bass + trout + blue_gill
    result = total_fish
    return result

print(solution())