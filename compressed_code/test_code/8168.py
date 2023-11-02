def solution():
    
    initial_length = 20
    percent_shorter = 30
    new_length = initial_length * (100 - percent_shorter) / 100
    result = new_length
    return result

print(solution())