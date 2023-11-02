def solution():
    key_lime_juice_doubled = 1/4 + 1/4
    tablespoons_per_cup = 16
    key_lime_juice_needed = key_lime_juice_doubled * tablespoons_per_cup
    tablespoons_per_key_lime = 1
    key_limes_needed = key_lime_juice_needed / tablespoons_per_key_lime
    result = key_limes_needed
    return result

print(solution())