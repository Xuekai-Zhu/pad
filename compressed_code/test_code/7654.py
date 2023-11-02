def solution():
    
    pencils_price = 0.5
    folders_price = 0.9
    pencils_per_dozen = 12
    pencils_needed = 2 * pencils_per_dozen
    folders_needed = 20
    total_cost = (pencils_needed * pencils_price) + (folders_needed * folders_price)
    result = total_cost
    return result

print(solution())