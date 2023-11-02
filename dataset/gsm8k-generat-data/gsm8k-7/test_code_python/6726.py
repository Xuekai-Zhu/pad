def solution():
    current_lines = 24
    added_lines_per_month = 3
    target_lines = 90

    # Calculate how many lines need to be added
    lines_to_add = target_lines - current_lines

    # Calculate how many months it will take to add those lines
    months_to_add_lines = lines_to_add / added_lines_per_month

    result = months_to_add_lines
    return result

print(solution())