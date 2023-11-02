def solution():
    """Sandy wants to lose as much weight as Joey does but needs 4 weeks to lose the same amount of weight that Joey loses in a single week. If Joey loses 8 pounds in 4 weeks, how many weeks will it take Sandy to lose the same amount of weight?"""
    joey_weight_loss_per_week = 8 / 4
    sandy_weight_loss_per_week = joey_weight_loss_per_week
    sandy_weeks_to_lose_weight = 4
    joey_weeks_to_lose_weight = 1
    sandy_weight_loss = sandy_weight_loss_per_week * sandy_weeks_to_lose_weight
    result = joey_weeks_to_lose_weight * sandy_weight_loss / sandy_weight_loss_per_week
    return result

print(solution())