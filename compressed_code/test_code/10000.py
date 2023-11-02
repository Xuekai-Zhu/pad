def solution():
    
    total_apples = 20
    jane_apples = 5
    james_apples = jane_apples + 2
    remaining_apples = total_apples - jane_apples - james_apples - 4
    result = remaining_apples
    return result

print(solution())