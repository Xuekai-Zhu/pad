def solution():
    """Onum Lake has 25 more trout than Boast Pool.   There are 75 fish in Boast Pool.  Riddle Pond has half as many fish as Onum Lake.  What is the average number of fish in all three bodies of water?"""
    # Define the number of fish in Boast Pool and the difference in number of fish between Onum Lake and Boast Pool
    BOAST_POOL_FISH = 75
    ONUM_BOAST_DIFF = 25

    # Calculate the number of fish in Onum Lake and Riddle Pond
    ONUM_LAKE_FISH = BOAST_POOL_FISH + ONUM_BOAST_DIFF
    RIDDLE_POND_FISH = ONUM_LAKE_FISH / 2

    # Calculate the total number of fish
    total_fish = BOAST_POOL_FISH + ONUM_LAKE_FISH + RIDDLE_POND_FISH

    # Calculate the average number of fish
    average_fish = total_fish / 3

    # Display the average number of fish
    result = average_fish
    return result

print(solution())