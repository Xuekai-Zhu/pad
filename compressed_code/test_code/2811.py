def solution():
    
    quarters_per_machine = 80
    dimes_per_machine = 100
    value_per_quarter = 0.25
    value_per_dime = 0.1
    total_value_per_machine = quarters_per_machine * value_per_quarter + dimes_per_machine * value_per_dime
    total_value = 90
    num_machines = total_value / total_value_per_machine
    result = num_machines
    return result

print(solution())