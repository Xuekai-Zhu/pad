def solution():
    pages_on_night_1 = 30
    pages_on_night_2 = 2 * pages_on_night_1 - 2
    pages_on_night_3 = pages_on_night_1 + pages_on_night_2 + 3
    total_pages = pages_on_night_1 + pages_on_night_2 + pages_on_night_3
    result = total_pages
    return result

print(solution())