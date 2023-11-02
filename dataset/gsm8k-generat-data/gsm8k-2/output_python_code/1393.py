def solution():
    """Jen has 10 more ducks than four times the number of chickens. If Jen has 150 ducks, how many total birds does she have?"""
    duck_count = 150
    chicken_count = (duck_count - 10) / 4
    total_birds = duck_count + chicken_count
    result = total_birds
    return result

print(solution())