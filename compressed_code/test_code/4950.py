def solution():
    
    price_per_meter = 0.20
    fence_length = 500
    num_fences = 50
    total_length = fence_length * num_fences
    total_earnings = total_length * price_per_meter
    result = total_earnings
    return result

print(solution())