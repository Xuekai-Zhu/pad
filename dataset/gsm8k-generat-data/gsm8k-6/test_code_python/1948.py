def solution():
    # Calculate the total revenue from small and medium cups
    total_small_medium_revenue = 11 + 24
    
    # Calculate the total number of large cups sold
    total_large_cups_sold = (50 - total_small_medium_revenue) / 3
    
    result = total_large_cups_sold
    return result

print(solution())