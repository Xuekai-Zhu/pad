def solution():
    # Define the amount of soda Rebecca drinks in a day and the number of packs she bought
    soda_per_day = 0.5
    packs = 3
    
    # Calculate the total number of bottles of soda Rebecca has
    bottles_total = packs * 6
    
    # Calculate the number of bottles Rebecca drinks in four weeks
    bottles_consumed = 4 * 7 * soda_per_day
    
    # Calculate the remaining number of bottles
    bottles_remaining = bottles_total - bottles_consumed
    
    result = bottles_remaining
    return result

print(solution())