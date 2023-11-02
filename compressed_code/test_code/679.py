def solution():
    
    ropes = [8, 20, 2, 2, 2, 7]
    knot_loss = 1.2
    total_length = sum(ropes) - knot_loss * (len(ropes) - 1)
    result = total_length
    return result

print(solution())