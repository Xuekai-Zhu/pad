def solution():
    """A wildlife team is monitoring the number of birds in a park. There are 3 blackbirds in each of the park’s 7 trees. There are also 13 magpies roaming around the park. How many birds are in the park in total?"""
    # Calculate the total number of blackbirds
    blackbirds = 3 * 7

    # Add the number of magpies
    total_birds = blackbirds + 13

    result = total_birds
    return result

print(solution())