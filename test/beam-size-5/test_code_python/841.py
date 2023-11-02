def solution():
    
    total_students = 20
    good_at_math_only = 5
    good_at_english_only = 8
    good_at_both = total_students - good_at_math_only - good_at_english_only
    result = good_at_both
    return result

print(solution())