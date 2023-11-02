def solution():
    """Matt orders 15 pounds of beef. He cuts that into 12-ounce steaks. How many steaks does he get?"""
    pounds_of_beef = 15
    ounces_of_beef = pounds_of_beef * 16
    ounces_per_steak = 12
    total_steaks = ounces_of_beef / ounces_per_steak
    result = total_steaks
    return result

print(solution())