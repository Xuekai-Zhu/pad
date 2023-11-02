def solution():
    """Apollo pulls the sun across the sky every night. Once a month, his fiery chariot’s wheels need to be replaced. He trades golden apples to Hephaestus the blacksmith to get Hephaestus to make him new wheels. Hephaestus raised his rates halfway through the year and now demands twice as many golden apples as before. He charged three golden apples for the first six months. How many golden apples does Apollo have to pay for the entire year of chariot wheels?"""
    wheels_per_month = 1
    months_per_year = 12
    rate_before_change = 3
    rate_after_change = rate_before_change * 2
    total_apples = (rate_before_change * (months_per_year // 2)) + (rate_after_change * (months_per_year // 2))
    result = total_apples
    return result

print(solution())