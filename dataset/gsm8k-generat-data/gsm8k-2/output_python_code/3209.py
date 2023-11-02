def solution():
    """Anna has a certain number of phone chargers and five times more laptop chargers than phone chargers. If she has 24 chargers total, how many phone chargers does she have?"""
    total_chargers = 24
    laptop_chargers = total_chargers / 6
    phone_chargers = total_chargers - laptop_chargers
    result = phone_chargers
    return result

print(solution())