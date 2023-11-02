def solution():
    weight_bench = 1000
    safety_margin = 0.2  # 20% safety margin
    user_weight = 250

    # Calculate the maximum weight John can lift with the safety margin
    max_weight = (weight_bench * (1 - safety_margin)) - user_weight
    result = max_weight
    return result

print(solution())