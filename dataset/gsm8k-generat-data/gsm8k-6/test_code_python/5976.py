def solution():
    # Calculate how much length of sub is left to buy after purchasing two 8 inch subs
    remaining_length = 81 - 2*8  
    
    # Calculate the number of 5 inch subs needed to make up the remaining length
    num_5_inch_subs = (remaining_length // 5) + (remaining_length % 5 > 0)  
    # The second part of this equation adds 1 if there is a remaining length that is not a multiple of 5 inches
    
    result = num_5_inch_subs
    return result

print(solution())