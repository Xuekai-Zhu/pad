def solution():
    """There are 20 students in Miss Susan's class. 5 of them are good at math only, 8 of them perform well in English only, and the rest are good at both math and English. How many are good at math?"""
    total_students = 20
    math_only = 5
    english_only = 8
    math_and_english = total_students - math_only - english_only
    math = math_only + math_and_english
    result = math
    return result

print(solution())