def solution():
    num_quarters_per_machine = 80
    num_dimes_per_machine = 100
    total_money = 90

    # Calculate the total value of all quarters in all machines
    total_quarters_value = num_quarters_per_machine * 0.25

    # Calculate the total value of all dimes in all machines
    total_dimes_value = num_dimes_per_machine * 0.1

    # Calculate the total value of one machine
    machine_value = total_quarters_value + total_dimes_value

    # Calculate the number of machines
    num_machines = total_money / machine_value
    result = num_machines
    return result

print(solution())