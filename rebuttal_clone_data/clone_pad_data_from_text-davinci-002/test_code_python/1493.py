def solution():
    first_leg = 100
    second_leg = 300
    total_distance = first_leg + second_leg
    first_leg_time = 1
    second_leg_time = total_distance / 50 
    total_time = first_leg_time + second_leg_time
    result = total_time
    return result

print(solution())