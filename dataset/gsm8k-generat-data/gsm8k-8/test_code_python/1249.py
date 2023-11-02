def solution():
    # Define the initial charge and desired charge
    initial_charge = 0
    desired_charge = 100

    # Calculate the percentage increase in charge per minute
    charge_per_minute = 100 / 60 * 0.25

    # Calculate the time required to reach the desired charge
    time_required = (desired_charge - initial_charge) / charge_per_minute

    result = time_required - 45 # subtract the initial 45 minutes
    return result

print(solution())