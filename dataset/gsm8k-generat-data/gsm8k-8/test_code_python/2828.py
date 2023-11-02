def solution():
    adam_magnets = 18

    # Calculate the number of magnets Adam gave away
    adam_gave_away = adam_magnets / 3

    # Calculate the number of magnets Adam had after giving some away
    adam_left = adam_magnets - adam_gave_away

    # Calculate the number of magnets Peter has
    peter_magnets = adam_left * 2

    result = peter_magnets
    return result

print(solution())