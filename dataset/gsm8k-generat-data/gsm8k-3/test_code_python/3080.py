def solution():
    """Tony has two fish. Every year, his parents buy him two more, but one of them dies. How many fish will he have in five years?"""
    # Define the starting number of fish
    fish_count = 2

    # Loop through five years of fish buying and dying
    for i in range(5):
        # Buy two fish
        fish_count += 2
        # One fish dies
        fish_count -= 1

    # Display the total number of fish after five years
    result = fish_count
    return result

print(solution())