def solution():
    dave_time = 10
    chuck_time = dave_time * 5
    erica_percent = 30

    # Calculate Chuck's max riding time
    chuck_max_time = chuck_time

    # Calculate Erica's max riding time
    erica_max_time = chuck_max_time * (1 + erica_percent/100)

    result = erica_max_time
    return result

print(solution())