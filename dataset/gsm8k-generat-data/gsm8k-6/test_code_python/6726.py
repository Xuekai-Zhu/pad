def solution():
    # Calculate the number of months it will take to reach 90 lines in the poem
    current_lines = 24
    added_lines = 3
    months = (90 - current_lines) / added_lines
    result = months
    return result

print(solution())