def solution():
    
    total_apples = 55
    father_apples = 10
    remaining_apples = total_apples - father_apples
    friends = 4
    apples_per_person = remaining_apples / (1 + friends)
    result = apples_per_person
    return result

print(solution())