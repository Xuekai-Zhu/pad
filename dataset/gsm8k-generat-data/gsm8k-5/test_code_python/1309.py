def solution():
    goldfish = 18  # Martin starts with 18 goldfish
    fish_lost = 5  # 5 goldfish die each week
    fish_added = 3  # Martin purchases 3 new goldfish each week
    weeks = 7  # Martin wants to know the total number of goldfish in 7 weeks

    # Calculate the total change in goldfish over the 7 weeks
    total_change = (fish_added - fish_lost) * weeks
    
    # Calculate the total number of goldfish after 7 weeks
    total_goldfish = goldfish + total_change
    result = total_goldfish
    return result

print(solution())