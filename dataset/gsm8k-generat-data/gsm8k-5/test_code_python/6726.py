def solution():
    current_lines = 24  # The epic poem currently contains 24 lines
    added_lines_per_month = 3  # A person adds 3 lines to the poem every month
    target_lines = 90  # The poem needs to contain 90 lines

    # Calculate the number of months needed to reach the target number of lines
    months_needed = (target_lines - current_lines) / added_lines_per_month
    result = months_needed
    return result

print(solution())