def solution():
    cost_per_meter = 0.20
    num_fences = 50
    fence_length = 500

    # Calculate the total length of all fences
    total_length = num_fences * fence_length

    # Calculate the total amount earned by Emmalyn
    total_earned = total_length * cost_per_meter
    result = total_earned
    return result

print(solution())