def solution():
    
    quarters_per_machine = 80
    dimes_per_machine = 100
    total_change = 90
    value_per_machine = (quarters_per_machine * 0.25) + (dimes_per_machine * 0.10)
    num_machines = total_change / value_per_machine
    result = num_machines
    return result

print(solution())