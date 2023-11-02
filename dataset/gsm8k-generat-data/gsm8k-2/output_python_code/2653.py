def solution():
    """Jack bought 55 apples. He wants to give 10 to his father and then equally share the remaining apples between him and his 4 friends. How many apples will each of them get?"""
    total_apples = 55
    father_apples = 10
    remaining_apples = total_apples - father_apples
    friends = 4
    apples_per_person = remaining_apples / (1 + friends)
    result = apples_per_person
    return result

print(solution())