def solution():
    # Define the rate of Machine A
    machine_a_rate = 12

    # Calculate the rate of Machine B and C
    machine_b_rate = machine_a_rate - 2
    machine_c_rate = machine_b_rate + 5

    # Calculate the total bottles capped in 10 minutes
    total_bottles = (machine_a_rate + machine_b_rate + machine_c_rate) * 10

    result = total_bottles
    return result

print(solution())