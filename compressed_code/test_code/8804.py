def solution():
    
    initial_necklaces = 50
    broken_necklaces = 3
    new_necklaces = 5
    gifted_necklaces = 15
    remaining_necklaces = initial_necklaces - broken_necklaces + new_necklaces - gifted_necklaces
    result = remaining_necklaces
    
    return result

print(solution())