def solution():
    """Each frog needs to eat 30 flies per day to live. Each fish needs to eat 8 frogs per day to live. Each gharial needs to eat 15 fish a day to live. How many flies get eaten every day in this swamp if it has 9 gharials?"""
    gharial_count = 9
    fish_count = gharial_count * 15
    frog_count = fish_count * 8
    total_flies = frog_count * 30
    result = total_flies
    return result

print(solution())