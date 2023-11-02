def solution():
    """Ruby is 6 times older than Sam. In 9 years, Ruby will be 3 times as old as Sam. How old is Sam now?"""
    ratio = 6
    future_ratio = 3
    time = 9
    difference_in_ratio = ratio - future_ratio
    sam_age = difference_in_ratio * time
    current_age = sam_age + time
    result = current_age
    return result

print(solution())