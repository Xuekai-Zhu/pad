def solution():
    """Erin runs her own launderette and needs to cash in the change from the machines. There are 80 quarters and 100 dimes in every machine in the launderette. When Erin empties all of the machines and cashes in the change, she has a total of $90. She had no money before she emptied the machines and each machine held the same amount of money. How many machines are in the launderette?"""
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