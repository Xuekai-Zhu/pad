def solution():
    # Calculate the total number of baby spoons Lisa has
    baby_spoons = 4 * 3  # Each child had 3 spoons

    # Calculate the total number of spoons Lisa has now
    total_spoons = baby_spoons + 2 + 10  # 2 decorative spoons and 10 large spoons

    # Add the teaspoons to the total number of spoons
    total_spoons += 15

    result = total_spoons
    return result

print(solution())