def solution():
    """Travis is hired to take 638 bowls from the factory to the home goods store. The home goods store will pay the moving company a $100 fee, plus $3 for every bowl that is delivered safely. Travis must pay the home goods store $4 each for any bowls that are lost or broken. If 12 bowls are lost, 15 bowls are broken, and the rest are delivered safely, how much should Travis be paid?"""
    total_bowls = 638
    bowls_delivered_safely = total_bowls - 12 - 15
    fee_per_bowl_safely_delivered = 3
    fee_for_safe_delivery = bowls_delivered_safely * fee_per_bowl_safely_delivered
    cost_per_lost_or_broken_bowl = 4
    cost_for_lost_bowls = 12 * cost_per_lost_or_broken_bowl
    cost_for_broken_bowls = 15 * cost_per_lost_or_broken_bowl
    total_cost_for_lost_or_broken_bowls = cost_for_lost_bowls + cost_for_broken_bowls
    total_payment = fee_for_safe_delivery - total_cost_for_lost_or_broken_bowls + 100
    result = total_payment
    return result

print(solution())