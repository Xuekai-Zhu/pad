def solution():
    
    top_jumpers = [23, 27, 28]
    average_jump = sum(top_jumpers) / len(top_jumpers)
    ravi_jump = 1.5 * average_jump
    result = ravi_jump
    return result

print(solution())