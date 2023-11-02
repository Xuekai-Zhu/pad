def solution():
    initial_charge = 0  # Nick's cell phone was initially empty
    target_charge = 100  # Nick wants to charge his phone to 100%
    time_to_reach_25 = 45  # It took 45 minutes to reach a 25% charge
    charge_reached = 25  # The cell phone has reached a 25% charge

    # Calculate the time needed to reach a 100% charge
    time_to_reach_100 = (target_charge - charge_reached) / 75 * time_to_reach_25

    result = time_to_reach_100
    return result

print(solution())