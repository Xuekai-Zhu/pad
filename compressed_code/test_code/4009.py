def solution():
    
    height = 60
    leg_length = height * 1/3
    head_length = height * 1/4
    body_length = height - leg_length - head_length
    result = body_length
    return result

print(solution())