def solution():
    liza_pages_per_hour = 20
    suzie_pages_per_hour = 15
    hours = 3
    liza_total_pages = liza_pages_per_hour * hours
    suzie_total_pages = suzie_pages_per_hour * hours
    difference = liza_total_pages - suzie_total_pages
    result = difference
    return result

print(solution())