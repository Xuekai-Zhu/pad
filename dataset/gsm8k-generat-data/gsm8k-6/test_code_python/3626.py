def solution():
    # Calculate the total value of coins in each machine
    machine_value = 80 * 0.25 + 100 * 0.1  # 80 quarters is $20, 100 dimes is $10

    # Calculate the number of machines needed to make $90
    num_machines = int(90 / machine_value)  # round down to the nearest integer

    result = num_machines
    return result

print(solution())