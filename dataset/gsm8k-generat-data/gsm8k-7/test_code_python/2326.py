def solution():
    amanda_flowers = 20
    peter_flowers = amanda_flowers * 3
    peter_gave_away = 15

    # Calculate the number of flowers left in Peter's garden after giving some away
    num_flowers_left = peter_flowers - peter_gave_away
    result = num_flowers_left
    return result

print(solution())