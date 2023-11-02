def solution():
    total_cents = 70
    num_dimes = 0
    num_nickels = 0
    
    while True:
        # increment number of nickels and dimes
        num_nickels += 1
        num_dimes += 1
        
        # calculate values in cents
        value_nickels = num_nickels * 5
        value_dimes = num_dimes * 10
        
        # check if values add up to total_cents and if num_dimes is 4 more than num_nickels
        if value_nickels + value_dimes == total_cents and num_dimes == num_nickels + 4:
            result = num_nickels
            break
    
    return result

print(solution())