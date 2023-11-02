def solution():
    weight_bench = 1000  # The weight bench can support 1000 pounds
    safety_margin = 0.2  # John wants to stay 20% under the weight bench limit for safety
    john_weight = 250  # John weighs 250 pounds

    # Calculate the maximum weight John can put on the bar
    max_weight = (weight_bench * (1 - safety_margin)) - john_weight
    result = max_weight
    return result

print(solution())