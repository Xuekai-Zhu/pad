def solution():
    # Calculate the total number of hours worked by the cobbler in a week
    total_hours = 8 * 4 + 3  # from Monday to Thursday: 8 hours each day, on Friday: 3 hours

    # Calculate the total number of pairs of shoes mended by the cobbler in a week
    total_pairs = 3 * total_hours  # the cobbler can mend 3 pairs of shoes in an hour
    result = total_pairs
    return result

print(solution())