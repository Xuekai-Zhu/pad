def solution():
    adam_magnets = 18  # Adam's starting number of magnets
    given_away = adam_magnets // 3  # Adam gives away a third of his magnets
    remaining = adam_magnets - given_away  # Adam's remaining magnets
    peter_magnets = remaining * 2  # Peter has twice as many magnets as Adam's remaining magnets
    result = peter_magnets
    return result

print(solution())