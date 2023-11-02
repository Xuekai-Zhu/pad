def solution():
    """Onum Lake has 25 more trout than Boast Pool. There are 75 fish in Boast Pool. Riddle Pond has half as many fish as Onum Lake. What is the average number of fish in all three bodies of water?"""
    # Calculate the number of fish in Onum Lake
    onum_fish = 75 + 25

    # Calculate the number of fish in Riddle Pond
    riddle_fish = onum_fish / 2

    # Calculate the total number of fish
    total_fish = onum_fish + riddle_fish + 75

    # Calculate the average number of fish
    average_fish = total_fish / 3

    result = average_fish
    return result

print(solution())