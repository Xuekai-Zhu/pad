def solution():
    """Each frog needs to eat 30 flies per day to live. Each fish needs to eat 8 frogs per day to live. Each gharial needs to eat 15 fish a day to live. How many flies get eaten every day in this swamp if it has 9 gharials?"""
    flies_per_frog = 30
    frogs_per_fish = 8
    fish_per_gharial = 15
    gharials = 9
    flies_eaten_per_day = gharials * fish_per_gharial * frogs_per_fish * flies_per_frog
    result = flies_eaten_per_day
    return result

print(solution())