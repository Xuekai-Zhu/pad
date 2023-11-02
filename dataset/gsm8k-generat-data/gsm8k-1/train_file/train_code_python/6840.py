def solution():
    """Janet takes two multivitamins and 3 calcium supplements every day for the first 2 weeks of the month. For the last two weeks of the month, she runs low on calcium supplements and only takes one per day. How many pills does Janet take in that month?"""
    multivitamins_per_day = 2
    calcium_supplements_per_day_first_half = 3
    calcium_supplements_per_day_second_half = 1
    days_in_month = 30
    days_in_first_half = 14
    days_in_second_half = 16
    
    total_multivitamins = multivitamins_per_day * days_in_month
    total_calcium_first_half = calcium_supplements_per_day_first_half * days_in_first_half
    total_calcium_second_half = calcium_supplements_per_day_second_half * days_in_second_half
    
    total_pills = total_multivitamins + total_calcium_first_half + total_calcium_second_half
    result = total_pills
    
    return result

print(solution())