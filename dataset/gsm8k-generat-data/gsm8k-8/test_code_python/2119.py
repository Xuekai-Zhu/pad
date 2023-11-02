def solution():
    # Calculate how many oranges each student would get if none had to be thrown away
    oranges_per_student = 108 / 12

    # Calculate how many oranges each student will get now
    oranges_after_discard = (108 - 36) / 12

    # Calculate the difference
    difference = oranges_per_student - oranges_after_discard
    result = difference
    return result

print(solution())