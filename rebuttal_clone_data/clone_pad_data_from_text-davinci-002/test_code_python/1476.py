def solution():
    bridge_weight_limit = 100
    kelly_weight = 34
    mike_weight = kelly_weight + 5
    megan_weight = mike_weight + ((mike_weight - kelly_weight) / 2)
    total_weight = kelly_weight + mike_weight + megan_weight
    over_weight = total_weight - bridge_weight_limit
    result = over_weight
    return result

print(solution())