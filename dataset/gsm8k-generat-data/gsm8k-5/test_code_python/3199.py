def solution():
    # Each sonnet is 14 lines long
    lines_per_sonnet = 14

    # Horatio read 7 sonnets to his lady fair, which equals 7 * 14 = 98 lines
    lines_read = 98

    # Horatio wrote 70 lines that his lady fair never heard
    lines_unread = 70

    # The total number of lines Horatio wrote is the sum of lines read and lines unread
    total_lines = lines_read + lines_unread

    # The total number of sonnets is the total number of lines divided by lines per sonnet
    total_sonnets = total_lines / lines_per_sonnet

    result = total_sonnets

    return result

print(solution())