def solution():
    bridge_capacity = 100
    kelly_weight = 34
    megan_weight = kelly_weight / 0.85  # 15% less weight than Kelly
    mike_weight = megan_weight + 5  # 5 kg more weight than Megan

    total_weight = kelly_weight + megan_weight + mike_weight
    excess_weight = total_weight - bridge_capacity
    result = excess_weight
    return result

print(solution())