def solution():
    """Camille saw 3 cardinals and four times as many robins as cardinals while bird watching. She also saw twice as many blue jays as cardinals and 1 more than three times as many sparrows as cardinals. How many birds did Camille see?"""
    cardinals = 3
    robins = 4 * cardinals
    blue_jays = 2 * cardinals
    sparrows = (3 * cardinals) + 1
    total_birds = cardinals + robins + blue_jays + sparrows
    result = total_birds
    return result

print(solution())