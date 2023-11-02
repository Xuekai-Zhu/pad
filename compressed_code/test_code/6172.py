def solution():
    
    price_per_slice = 3
    slices_per_pie = 10
    num_pies = 6
    total_slices = slices_per_pie * num_pies
    money_earned = total_slices * price_per_slice
    result = money_earned
    return result

print(solution())