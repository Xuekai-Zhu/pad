def solution():
    """Onum Lake has 25 more trout than Boast Pool. There are 75 fish in Boast Pool. Riddle Pond has half as many fish as Onum Lake. What is the average number of fish in all three bodies of water?"""
    boast_pool_fish = 75
    onum_lake_fish = boast_pool_fish + 25
    riddle_pond_fish = onum_lake_fish / 2
    total_fish = boast_pool_fish + onum_lake_fish + riddle_pond_fish
    average_fish = total_fish / 3
    result = average_fish
    return result

print(solution())