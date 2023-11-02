def solution():
    """During a race transmitted on television, five advertisements were shown, lasting 3 minutes each. One minute of advertising costs $4000. What was the cost of transmitting these advertisements during the race?"""
    ads_shown = 5
    ad_length = 3
    cost_per_minute = 4000
    total_cost = ads_shown * ad_length * cost_per_minute
    result = total_cost
    return result

print(solution())