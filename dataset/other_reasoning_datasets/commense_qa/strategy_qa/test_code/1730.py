def solution():
    initial_troop_count = 75000
    intended_increase = 125000 - 75000
    if intended_increase <= 75000:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())