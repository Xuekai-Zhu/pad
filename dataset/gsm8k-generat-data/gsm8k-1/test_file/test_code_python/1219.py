def solution():
    """To make a call from a payphone, you must pay $0.25 for each minute of your call. After 16 minutes, that price drops to $0.2 per minute. How much would a 36-minute call cost?"""
    cost_per_minute1 = 0.25
    cost_per_minute2 = 0.2
    minutes1 = 16
    minutes2 = 36 - minutes1
    total_cost = (cost_per_minute1 * minutes1) + (cost_per_minute2 * minutes2)
    result = total_cost
    return result

print(solution())