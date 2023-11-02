def solution():
    """Each frog needs to eat 30 flies per day to live. Each fish needs to eat 8 frogs per day to live. Each gharial needs to eat 15 fish a day to live. How many flies get eaten every day in this swamp if it has 9 gharials?"""
    # Calculate the number of fish needed to feed one gharial per day
    fish_per_gharial = 15

    # Calculate the number of frogs needed to feed one fish per day
    frogs_per_fish = 8

    # Calculate the number of flies needed to feed one frog per day
    flies_per_frog = 30

    # Calculate the number of flies needed to feed one gharial per day
    flies_per_gharial = fish_per_gharial * frogs_per_fish * flies_per_frog

    # Calculate the total number of flies needed to feed all gharials per day
    flies_per_day = flies_per_gharial * 9

    # return the result
    result = flies_per_day
    return result

print(solution())