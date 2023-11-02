def solution():
    """Travis is hired to take 638 bowls from the factory to the home goods store. The home goods store will pay the moving company a $100 fee, plus $3 for every bowl that is delivered safely. Travis must pay the home goods store $4 each for any bowls that are lost or broken. If 12 bowls are lost, 15 bowls are broken, and the rest are delivered safely, how much should Travis be paid?"""
    total_bowls = 638
    safe_bowls = total_bowls - 12 - 15
    fee = 100
    safe_bowl_fee = 3 * safe_bowls
    broken_bowl_fee = 4 * 15
    total_fee = fee + safe_bowl_fee - broken_bowl_fee
    result = total_fee
    return result

print(solution())