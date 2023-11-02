def solution():
    # Define the production rate of each machine
    production_rate_per_machine = 10

    # Define the desired total production rate
    desired_total_production_rate = 50

    # Calculate the number of machines required to achieve the desired total production rate
    required_number_of_machines = desired_total_production_rate / production_rate_per_machine
    result = required_number_of_machines
    return result

print(solution())