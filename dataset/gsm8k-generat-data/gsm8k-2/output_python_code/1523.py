def solution():
    """Max attended 40 college courses in 2 years. Sid attended four times as many college courses as Max in the same period. What's the total of college courses they both attended?"""
    max_courses = 40
    sid_courses = 4 * max_courses
    total_courses = max_courses + sid_courses
    result = total_courses
    return result

print(solution())