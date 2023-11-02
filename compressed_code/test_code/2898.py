def solution():
    
    cardinals = 3
    robins = 4 * cardinals
    blue_jays = 2 * cardinals
    sparrows = 3 * cardinals + 1
    total_birds = cardinals + robins + blue_jays + sparrows
    result = total_birds
    return result

print(solution())