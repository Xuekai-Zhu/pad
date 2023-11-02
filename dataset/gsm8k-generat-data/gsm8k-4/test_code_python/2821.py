def solution():
    """Matt orders 15 pounds of beef. He cuts that into 12-ounce steaks. How many steaks does he get?"""
    # Convert pounds to ounces
    beef_ounces = 15 * 16

    # Calculate the number of 12-ounce steaks
    num_steaks = beef_ounces // 12

    result = num_steaks
    return result

print(solution())