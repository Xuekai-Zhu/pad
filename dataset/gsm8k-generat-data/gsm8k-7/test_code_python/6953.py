def solution():
    total_wax = 0
    
    # Calculate the total amount of wax left in the 20 oz candles
    total_wax += 5 * 20 * 0.1
    
    # Calculate the total amount of wax left in the 5 oz candles
    total_wax += 5 * 5 * 0.1
    
    # Calculate the total amount of wax left in the 1 oz candles
    total_wax += 25 * 1 * 0.1
    
    # Calculate the total number of 5 oz candles she can make
    num_candles = total_wax / 0.5
    
    result = num_candles
    return result

print(solution())