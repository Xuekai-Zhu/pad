def solution():
    """A fisherman catches 3 types of fish in his net.  There are 32 bass, 1/4 as many trout as bass, and double the number of blue gill as bass.  How many fish did the fisherman catch total?"""
    # Calculate number of trout and blue gill
    bass = 32
    trout = bass / 4
    blue_gill = bass * 2

    # Calculate total number of fish
    total_fish = bass + trout + blue_gill

    # Return the result
    result = total_fish
    return result

print(solution())