def solution():
    # Calculate the number of bottles Machine B can cap in 1 minute
    caps_b = 12 - 2

    # Calculate the number of bottles Machine C can cap in 1 minute
    caps_c = caps_b + 5

    # Calculate the total number of bottles those three machines can cap in 1 minute
    total_caps = 12 + caps_b + caps_c

    # Calculate the total number of bottles those three machines can cap in 10 minutes
    total_caps_10_min = total_caps * 10

    result = total_caps_10_min
    return result

print(solution())