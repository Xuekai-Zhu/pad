def solution():
    max_courses = 40  # Max attended 40 college courses in 2 years
    sid_courses = 4 * max_courses  # Sid attended four times as many courses as Max

    # Calculate the total number of college courses they both attended
    total_courses = max_courses + sid_courses
    result = total_courses
    return result

print(solution())