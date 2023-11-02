def solution():
    """Mary used 15 gallons of fuel this week. Last week she used 20% less. How much fuel did she use in total for the two weeks?"""
    gallons_used_this_week = 15
    percent_decrease = 20
    decrease_amount = gallons_used_this_week * (percent_decrease / 100)
    gallons_used_last_week = gallons_used_this_week - decrease_amount
    total_gallons_used = gallons_used_this_week + gallons_used_last_week
    result = total_gallons_used
    return result

print(solution())