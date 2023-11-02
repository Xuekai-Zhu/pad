def solution():
    gallons_per_flush_old = 5  # John's old toilet used 5 gallons of water per flush
    flushes_per_day = 15  # John's household flushed 15 times per day
    days_in_june = 30  # There are 30 days in June

    # Calculate the total amount of water used in June with the old toilet
    water_used_old = gallons_per_flush_old * flushes_per_day * days_in_june

    gallons_per_flush_new = gallons_per_flush_old * 0.2  # John's new toilet uses 80% less water per flush

    # Calculate the total amount of water used in June with the new toilet
    water_used_new = gallons_per_flush_new * flushes_per_day * days_in_june

    # Calculate the amount of water John saved in June
    water_saved = water_used_old - water_used_new
    result = water_saved
    return result

print(solution())