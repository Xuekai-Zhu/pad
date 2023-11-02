def solution():
    sunday = 4  # Alice bought 4 pints of ice cream on Sunday
    monday = 3 * sunday  # She bought 3 times that number on Monday
    tuesday = monday / 3  # On Tuesday she bought one-third the number of pints she bought the day before
    total = sunday + monday + tuesday  # Total number of pints she had before returning on Wednesday
    wednesday = total - (monday / 2)  # She returned half of the pints she bought on Monday because they were expired
    result = wednesday
    return result

print(solution())