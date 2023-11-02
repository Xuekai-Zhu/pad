def solution():
    """Baldur gets water from a well. He gets 5 pails of water every morning and 6 pails of water every afternoon. If each pail contains 5 liters of water, how many liters of water does he get every day?"""
    morning_pails = 5
    afternoon_pails = 6
    pail_size = 5
    total_liters = (morning_pails + afternoon_pails) * pail_size
    result = total_liters
    return result

print(solution())