def solution():
    
    slices_per_pie = 10
    price_per_slice = 3
    pies = 6
    total_slices = slices_per_pie * pies
    total_earnings = total_slices * price_per_slice
    result = total_earnings
    return result

print(solution())