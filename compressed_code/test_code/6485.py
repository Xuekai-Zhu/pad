def solution():
    
    ropes = [8, 20, 2, 2, 2, 7]
    knots = len(ropes) - 1
    total_length = sum(ropes) - (knots * 1.2)
    result = total_length
    return result

print(solution())