def solution():
    total_apples = 55
    father_apples = 10
    remaining_apples = total_apples - father_apples
    friends = 4

    # Divide the remaining apples equally among Jack and his friends
    apples_per_person = remaining_apples / (1 + friends)
    result = apples_per_person
    return result

print(solution())