def solution():
    
    lines_per_sonnet = 14
    lines_read = 7 * lines_per_sonnet
    lines_not_read = 70
    total_lines = lines_read + lines_not_read
    sonnets_written = total_lines / lines_per_sonnet
    result = sonnets_written
    return result

print(solution())