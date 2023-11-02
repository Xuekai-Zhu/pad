def solution():
    """Jen has 10 more ducks than four times the number of chickens. If Jen has 150 ducks, how many total birds does she have?"""
    total_ducks = 150
    ducks_to_chickens_ratio = 4
    extra_ducks = 10
    chickens = (total_ducks - extra_ducks) / ducks_to_chickens_ratio
    total_birds = chickens + total_ducks
    result = total_birds
    return result

print(solution())