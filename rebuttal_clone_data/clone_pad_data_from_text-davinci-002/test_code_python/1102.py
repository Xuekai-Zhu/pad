def solution():
    ceiling_tiles = 38
    books = 75
    times_counted_on_monday = 1
    times_counted_on_tuesday = ceiling_tiles * 2 + books * 3
    total_times_counted = times_counted_on_monday + times_counted_on_tuesday
    result = total_times_counted
    return result

print(solution())