def solution():
    # Calculate the total weight gained by the three family members
    Orlando_weight = 5
    Jose_weight = 2 + 2*Orlando_weight
    Fernando_weight = (1/2)*Jose_weight - 3
    total_weight = Orlando_weight + Jose_weight + Fernando_weight
    result = total_weight
    return result

print(solution())