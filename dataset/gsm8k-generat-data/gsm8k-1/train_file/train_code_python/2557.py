def solution():
    """James can make a beret from 3 spools of yarn. If he has 12 spools of red yarn, 15 spools of black yarn, and 6 spools of blue yarn, how many berets can he make?"""
    red_yarn = 12
    black_yarn = 15
    blue_yarn = 6
    spools_per_beret = 3
    total_berets = min(red_yarn, black_yarn, blue_yarn) // spools_per_beret
    result = total_berets
    return result

print(solution())