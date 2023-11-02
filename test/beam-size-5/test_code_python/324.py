def solution():
    charge_rate = 1/3  # The charge rate is 1% of charge per 3 minutes
    current_charge = 0.6 * current_charge  # The phone is at 60% charged
    total_charge = current_charge + current_charge  # The total charge to fully charge in hours

    # Calculate the time it will take to fully charge in hours
    time_in_hours = total_charge / 60
    result = time_in_hours
    return result

print(solution())