def solution():
    grade_range = range(1, 6) # Represents K-5th grade
    need_calculator = False
    if 5 in grade_range:
        need_calculator = False
    else:
        need_calculator = True
    return "yes" if need_calculator else "no"

print(solution())