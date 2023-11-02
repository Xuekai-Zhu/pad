def solution():
    """Max attended 40 college courses in 2 years. Sid attended four times as many college courses as Max in the same period. What's the total of college courses they both attended?"""
    # Define the number of courses Max attended
    max_courses = 40

    # Calculate the number of courses Sid attended
    sid_courses = max_courses * 4

    # Calculate the total number of courses they both attended
    total_courses = max_courses + sid_courses

    result = total_courses
    return result

print(solution())