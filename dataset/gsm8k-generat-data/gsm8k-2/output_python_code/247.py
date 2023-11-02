def solution():
    """Tony has a terrible toothache and decides to buy some painkillers from the store. He picks up a bottle of 50 pills and takes them home. He takes 2 pills each day three times a day for the first 2 days, before cutting this amount in half for the next 3 days. On the sixth day, he takes a final 2 pills in the morning and ends up feeling better. How many pills are left in the bottle?"""
    total_days = 6
    full_dose_days = 2
    half_dose_days = total_days - full_dose_days
    full_dose_amount = 2 * 3
    half_dose_amount = full_dose_amount / 2
    total_pills_taken = (full_dose_days * full_dose_amount) + (half_dose_days * half_dose_amount) + 2
    leftover_pills = 50 - total_pills_taken

    result = leftover_pills
    return result

print(solution())