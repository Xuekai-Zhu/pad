def solution():
    # Calculate total production in 23 hours with 3 machines
    total_production_3_machines = 3 * 23 * 2

    # Calculate total production in 12 hours with the new machine
    total_production_1_machine = 12 * 2

    # Calculate the total production after adding the new machine
    total_production = total_production_3_machines + total_production_1_machine

    # Calculate the total earnings for the day
    total_earnings = total_production * 50

    result = total_earnings
    return result

print(solution())