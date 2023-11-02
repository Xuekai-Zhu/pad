def solution():
    """A fisherman catches 3 types of fish in his net.  There are 32 bass, 1/4 as many trout as bass, and double the number of blue gill as bass.  How many fish did the fisherman catch total?"""
    # Define the number of bass caught and calculate the number of trout and blue gill caught
    bass = 32
    trout = bass / 4
    blue_gill = bass * 2

    # Calculate the total number of fish caught
    total_fish = bass + trout + blue_gill

    # Display the total number of fish caught
    result = total_fish
    return result

print(solution())