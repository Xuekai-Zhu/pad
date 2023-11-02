def solution():
    # Define the value of each quarter and dime
    quarter_value = 0.25
    dime_value = 0.10

    # Calculate the total value of the change in each machine
    machine_value = (80 * quarter_value) + (100 * dime_value)

    # Calculate the number of machines needed to equal the total amount earned by Erin
    machines_needed = 90 / machine_value

    result = machines_needed
    return result

print(solution())