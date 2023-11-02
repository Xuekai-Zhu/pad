def solution():
    """To let Ruth know how long her fish will live, her father tells her that well-cared fish can live 2 years longer than dogs live. On average, dogs live 4 times as long as hamsters live. And hamsters live an average of 2.5 years. How long can a fish live?"""
    hamster_life = 2.5
    dog_life = hamster_life * 4
    fish_life = dog_life + 2
    result = fish_life
    return result

print(solution())