def solution():
    """Nick's cell phone was initially empty but was then charged for 45 minutes and has reached a 25% charge. How much longer must the cell phone be charged to reach 100% charge?"""
    initial_charge = 0
    target_charge = 100
    current_charge = 25
    charge_per_minute = (target_charge - current_charge) / 45
    time_to_full_charge = (100 - current_charge) / charge_per_minute
    result = time_to_full_charge
    return result

print(solution())