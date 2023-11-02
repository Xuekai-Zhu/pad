def solution():
    """Nick's cell phone was initially empty but was then charged for 45 minutes and has reached a 25% charge. How much longer must the cell phone be charged to reach 100% charge?"""
    initial_charge = 0
    current_charge = 0.25
    time_until_current_charge = 45
    remaining_charge_needed = 1 - current_charge
    time_needed_to_complete_charge = (remaining_charge_needed / 0.25) * time_until_current_charge
    result = time_needed_to_complete_charge
    return result

print(solution())