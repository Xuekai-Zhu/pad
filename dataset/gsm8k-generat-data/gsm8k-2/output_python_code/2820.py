def solution():
    """Matt orders 15 pounds of beef. He cuts that into 12-ounce steaks. How many steaks does he get?"""
    beef_weight = 15 * 16  # convert pounds to ounces
    steak_weight = 12
    num_steaks = beef_weight // steak_weight
    result = num_steaks
    return result

print(solution())