def solution():
    """The epic poem currently contains 24 lines. If a person adds 3 lines to the poem every month, in how many months will the poem contain 90 lines?"""
    starting_lines = 24
    target_lines = 90
    lines_added_per_month = 3
    months_to_reach_target = (target_lines - starting_lines) / lines_added_per_month
    result = months_to_reach_target
    return result

print(solution())