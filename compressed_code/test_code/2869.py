def solution():
    
    machine_a_rate = 12
    machine_b_rate = machine_a_rate - 2
    machine_c_rate = machine_b_rate + 5
    total_bottles = (machine_a_rate + machine_b_rate + machine_c_rate) * 10
    result = total_bottles
    return result

print(solution())