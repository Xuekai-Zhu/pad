def solution():
    machine_a_rate = 12  # bottles per minute
    machine_b_rate = machine_a_rate - 2
    machine_c_rate = machine_b_rate + 5

    # Calculate the total bottles capped by all machines in 1 minute
    total_rate = machine_a_rate + machine_b_rate + machine_c_rate

    # Calculate the total bottles capped by all machines in 10 minutes
    total_bottles = total_rate * 10
    result = total_bottles
    return result

print(solution())