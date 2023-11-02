def solution():
    """The epic poem currently contains 24 lines. If a person adds 3 lines to the poem every month, in how many months will the poem contain 90 lines?"""
    current_lines = 24
    added_lines_per_month = 3
    target_lines = 90
    months_needed = (target_lines - current_lines) / added_lines_per_month
    result = months_needed
    return result

print(solution())