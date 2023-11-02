def solution():
    
    sheets_per_ream = 500
    price_per_ream = 27
    sheets_needed = 5000
    reams_needed = sheets_needed / sheets_per_ream
    total_cost = reams_needed * price_per_ream
    result = total_cost
    return result

print(solution())