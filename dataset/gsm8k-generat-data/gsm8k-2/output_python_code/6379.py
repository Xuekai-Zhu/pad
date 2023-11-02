def solution():
    """A local park has 70 pigeons that call the park home. Half of the pigeons are black, and 20 percent of the black pigeons are male. How many more black female pigeons are there than black male pigeons?"""
    total_pigeons = 70
    black_pigeons = total_pigeons / 2
    black_male_pigeons = black_pigeons * 0.2
    black_female_pigeons = black_pigeons - black_male_pigeons
    difference = black_female_pigeons - black_male_pigeons
    result = difference
    return result

print(solution())