def solution():
    
    bucket_sizes = [3, 5, 6]
    bucket_states = [0, 0, 0]  
    
    bucket_states[1] = 5
    
    amount_poured = min(bucket_states[1], bucket_sizes[0]-bucket_states[0])
    bucket_states[1] -= amount_poured
    bucket_states[0] += amount_poured
    
    amount_poured = min(bucket_states[1], bucket_sizes[2]-bucket_states[2])
    bucket_states[1] -= amount_poured
    bucket_states[2] += amount_poured
    
    max_amount = bucket_sizes[2] - bucket_states[2]
    result = max_amount
    return result

print(solution())