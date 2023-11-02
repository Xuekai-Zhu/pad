def solution():
    num_coins = 63
    
    # Let's use q, d, and n to represent the number of quarters, dimes, and nickels respectively
    # We know that d = q + 3 and n = q - 6
    
    q = (num_coins + 3) / 4 # We use the fact that there are 4 coins per set of (q, d, n)
    
    result = q
    return result

print(solution())