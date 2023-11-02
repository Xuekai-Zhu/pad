def solution():
    # Calculate the maximum weight John can lift while staying 20% under the weight limit of his bench
    weight_limit = 1000  # weight limit of the bench in pounds
    safety_margin = 0.2  # John wants to stay 20% under the weight limit for safety
    max_weight = (1 - safety_margin) * weight_limit  # maximum weight John can lift while staying 20% under the weight limit
    weight_on_bar = max_weight - 250  # subtract John's weight from the maximum weight he can lift
    result = weight_on_bar
    return result

print(solution())