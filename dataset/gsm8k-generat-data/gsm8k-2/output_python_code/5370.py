def solution():
    """Martha has 20 apples. She decided to split them among her friends. Jane got 5 apples from her, and James got 2 more than Jane. How many more apples would Martha need to give away to be left with only 4 of them?"""
    total_apples = 20
    jane_apples = 5
    james_apples = jane_apples + 2
    remaining_apples = total_apples - jane_apples - james_apples - 4
    result = remaining_apples
    return result

print(solution())