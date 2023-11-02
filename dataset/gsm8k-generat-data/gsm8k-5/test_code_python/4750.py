def solution():
    # Calculate the number of trout in Onum Lake
    trout_onum = 75 + 25  # Onum Lake has 25 more trout than Boast Pool

    # Calculate the total number of fish in all three bodies of water
    total_fish = trout_onum + 75 + (trout_onum / 2)  # Riddle Pond has half as many fish as Onum Lake

    # Calculate the average number of fish in all three bodies of water
    average_fish = total_fish / 3
    result = average_fish
    return result

print(solution())