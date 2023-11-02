def solution():
    
    total_people = 10
    total_days = 10
    total_coal = 10000
    half_people = total_people / 2
    target_coal = 40000
    shovel_rate = total_coal / (total_people * total_days)
    target_days = target_coal / (half_people * shovel_rate)
    result = target_days
    return result

print(solution())