def solution():
    """During a race transmitted on television, five advertisements were shown, lasting 3 minutes each. One minute of advertising costs $4000. What was the cost of transmitting these advertisements during the race?"""
    num_ads = 5
    ad_length = 3
    ad_cost_per_min = 4000
    total_ad_time = num_ads * ad_length
    total_ad_cost = total_ad_time * ad_cost_per_min
    result = total_ad_cost
    return result

print(solution())