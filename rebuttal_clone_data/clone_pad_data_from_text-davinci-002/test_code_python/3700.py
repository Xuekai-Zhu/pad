def solution():
    machine_a_speed = 12
    machine_b_speed = machine_a_speed - 2
    machine_c_speed = machine_b_speed + 5
    minutes = 10
    total_bottles = machine_a_speed * minutes + machine_b_speed * minutes + machine_c_speed * minutes
    result = total_bottles
    
    return result

print(solution())