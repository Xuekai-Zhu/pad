def solution():
    initial_tabs = 400
    closed_first = initial_tabs * 0.25
    remaining_after_first = initial_tabs - closed_first
    closed_second = remaining_after_first * 0.4
    remaining_after_second = remaining_after_first - closed_second
    closed_third = remaining_after_second * 0.5
    remaining_tabs = remaining_after_second - closed_third
    result = remaining_tabs
    return result

print(solution())