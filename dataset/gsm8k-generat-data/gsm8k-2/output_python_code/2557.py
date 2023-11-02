def solution():
    """James can make a beret from 3 spools of yarn. If he has 12 spools of red yarn, 15 spools of black yarn, and 6 spools of blue yarn, how many berets can he make?"""
    red_berets = 12 // 3
    black_berets = 15 // 3
    blue_berets = 6 // 3
    total_berets = red_berets + black_berets + blue_berets
    result = total_berets
    return result

print(solution())