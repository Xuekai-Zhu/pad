def solution():
    total_time = 150  # total time spent on homework
    math_time = 0.3 * total_time  # time spent on math
    science_time = 0.4 * total_time  # time spent on science
    other_time = total_time - math_time - science_time  # time spent on other subjects
    result = other_time
    return result

print(solution())