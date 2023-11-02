def solution():
    
    total_height = 60
    leg_length = total_height * (1/3)
    head_length = total_height * (1/4)
    body_length = total_height - leg_length - head_length
    result = body_length
    return result

print(solution())