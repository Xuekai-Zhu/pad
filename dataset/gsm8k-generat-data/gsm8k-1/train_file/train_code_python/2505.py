def solution():
    """Tom has only been getting 6 hours of sleep a day. He increases that by 1/3. How many hours of sleep does he get per night?"""
    current_sleep = 6
    increase = current_sleep * (1/3)
    new_sleep = current_sleep + increase
    result = new_sleep
    return result

print(solution())