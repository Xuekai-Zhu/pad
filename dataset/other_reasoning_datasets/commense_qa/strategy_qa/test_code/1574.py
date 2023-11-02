def solution():
    enrolled_year = 1961
    dropped_out_year = 1964
    moved_year = 1964
    if moved_year >= 1964 and (dropped_out_year < 1964 or dropped_out_year is None):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())