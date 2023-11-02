def solution():
    """Mariah’s grandma was teaching her to knit. Mariah used 1/4 of a skein of yarn. Her grandma used 1/2 of a skein of yarn. There are 364 yards in a skein of yarn. How many yards of yarn did they use altogether?"""
    skein_yards = 364
    mariah_yards = skein_yards * 1/4
    grandma_yards = skein_yards * 1/2
    total_yards = mariah_yards + grandma_yards
    result = total_yards
    return result

print(solution())