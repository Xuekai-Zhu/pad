def solution():
    value_per_machine = (80*0.25) + (100*0.10)  # Each machine has 80 quarters and 100 dimes, which equals $25.00
    total_value = 90  # Erin cashes in the change and gets $90.00
    num_machines = total_value / value_per_machine  # Calculate the number of machines
    result = num_machines
    return result

print(solution())