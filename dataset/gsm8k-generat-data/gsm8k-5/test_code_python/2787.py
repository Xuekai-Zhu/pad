def solution():
    ounces_per_bottle = 20  # Remi's water bottle holds 20 ounces
    times_refilled_per_day = 3  # Remi refills the bottle 3 times per day
    days = 7  # Remi wants to calculate his water intake over 7 days
    ounces_spilled = 5 + 8  # Remi spills 5 ounces one time and 8 ounces another time

    # Calculate the total number of ounces Remi drinks in a week
    total_ounces = (ounces_per_bottle - ounces_spilled) * times_refilled_per_day * days

    result = total_ounces
    return result

print(solution())