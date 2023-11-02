def solution():
    initial_floors = 20
    first_half_floors = initial_floors / 2
    second_half_floors = initial_floors - first_half_floors
    first_half_time = first_half_floors * 15
    second_half_time = second_half_floors * 5
    third_half_time = second_half_floors * 16
    total_time = first_half_time + second_half_time + third_half_time
    result = total_time / 60
    return result

print(solution())