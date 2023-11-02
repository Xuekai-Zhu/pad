def solution():
    """The cell-phone recharges at the rate of 1 percentage-point of charge per 3 minutes. Now, the phone is at 60% charged. How long will it take to fully charge, in hours?"""
    initial_charge = 60
    final_charge = 100
    percent_per_minute = 1/3
    minutes_to_full_charge = (final_charge - initial_charge) / percent_per_minute
    hours_to_full_charge = minutes_to_full_charge / 60
    result = hours_to_full_charge
    return result

print(solution())