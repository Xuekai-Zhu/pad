def solution():
    initial_ants = 50
    time = 5
    rate = 2
    ants_after_5_hours = initial_ants * (rate ** time)
    result = ants_after_5_hours
    return result

print(solution())