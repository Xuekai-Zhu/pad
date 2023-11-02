def solution():
    """Lee rears only sheep and geese on his farm. If the total number of animal legs is 70, and the total number of animal heads is 20, how many sheep live on Lee's farm?"""
    total_legs = 70
    total_heads = 20
    geese_legs = 2
    sheep_legs = 4
    geese = (total_legs - (sheep_legs * total_heads)) / (geese_legs - sheep_legs)
    sheep = total_heads - geese
    result = sheep
    return result

print(solution())