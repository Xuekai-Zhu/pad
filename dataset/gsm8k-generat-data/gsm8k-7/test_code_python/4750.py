def solution():
    # Find the number of trout in Onum Lake
    num_trout = 25 + 75
    
    # Find the total number of fish in Onum Lake and Boast Pool
    total_fish = num_trout + 75
    
    # Find the number of fish in Riddle Pond
    num_riddle_pond_fish = total_fish / 2
    
    # Find the total number of fish in all three bodies of water
    total_fish_all = num_trout + 75 + num_riddle_pond_fish
    
    # Find the average number of fish
    average_fish = total_fish_all / 3
    
    result = average_fish
    return result

print(solution())