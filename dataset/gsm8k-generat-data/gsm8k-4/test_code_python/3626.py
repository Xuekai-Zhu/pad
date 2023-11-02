def solution():
    """Erin runs her own launderette and needs to cash in the change from the machines. There are 80 quarters and 100 dimes in every machine in the launderette. When Erin empties all of the machines and cashes in the change, she has a total of $90. She had no money before she emptied the machines and each machine held the same amount of money. How many machines are in the launderette?"""
    # Define the value of a quarter and a dime
    QUARTER_VALUE = 0.25
    DIME_VALUE = 0.1

    # Define the total value of the change in each machine
    machine_value = (80 * QUARTER_VALUE) + (100 * DIME_VALUE)

    # Calculate the total number of machines in the launderette
    total_machines = int(90 / machine_value)

    result = total_machines
    return result

print(solution())