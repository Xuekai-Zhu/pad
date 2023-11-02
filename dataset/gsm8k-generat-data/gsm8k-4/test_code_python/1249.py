def solution():
    """Nick's cell phone was initially empty but was then charged for 45 minutes and has reached a 25% charge. How much longer must the cell phone be charged to reach 100% charge?"""
    # Define the initial charge and the target charge
    initial_charge = 0
    target_charge = 100

    # Define the current charge
    current_charge = 25

    # Define the time it took to reach the current charge
    time_to_reach_current_charge = 45

    # Calculate the percentage increase in charge per minute
    charge_per_minute = current_charge / time_to_reach_current_charge

    # Calculate the time required to reach the target charge
    time_to_reach_target_charge = (target_charge - current_charge) / charge_per_minute

    # return the result
    result = round(time_to_reach_target_charge)
    return result

print(solution())