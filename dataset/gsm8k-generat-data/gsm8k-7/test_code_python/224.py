def solution():
    first_scroll_age = 4080
    fifth_scroll_age = first_scroll_age * 2 - (first_scroll_age / 2) - (first_scroll_age / 4) - (first_scroll_age / 8) - (first_scroll_age / 16)
    result = fifth_scroll_age
    return result

print(solution())