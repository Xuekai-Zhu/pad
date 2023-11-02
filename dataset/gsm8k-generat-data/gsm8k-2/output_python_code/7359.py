def solution():
    """Apollo pulls the sun across the sky every night. Once a month, his fiery chariot’s wheels need to be replaced. He trades golden apples to Hephaestus the blacksmith to get Hephaestus to make him new wheels. Hephaestus raised his rates halfway through the year and now demands twice as many golden apples as before. He charged three golden apples for the first six months. How many golden apples does Apollo have to pay for the entire year of chariot wheels?"""
    first_half_cost = 3 * 6  # 3 golden apples per month for 6 months
    second_half_cost = 2 * first_half_cost  # Hephaestus doubled his rates
    total_cost = first_half_cost + second_half_cost
    result = total_cost
    return result

print(solution())