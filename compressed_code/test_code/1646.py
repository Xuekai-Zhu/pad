def solution():
    
    peanut_butter_price = 3
    almond_butter_price = 3 * 3
    butter_per_batch = 0.5
    cost_per_batch_pb = peanut_butter_price * butter_per_batch
    cost_per_batch_ab = almond_butter_price * butter_per_batch
    difference = cost_per_batch_ab - cost_per_batch_pb
    result = difference
    return result

print(solution())