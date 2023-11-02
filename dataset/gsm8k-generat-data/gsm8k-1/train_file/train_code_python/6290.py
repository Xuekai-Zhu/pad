def solution():
    """Andy had a platter of chocolate cookies. He ate 3 of them then gave his little brother 5 because he was behaving. He then handed the platter to his basketball team of eight members. The first player to arrive took 1, the second player to arrive took 3, the third player took 5, and so on. When the last player took his share, the platter was empty. How many chocolate cookies did Andy have from start with?"""
    cookies_at_start = 3 + 5  # ate 3 and gave 5 to brother
    for i in range(1, 9):
        cookies_at_start += 2*i - 1  # each player took 2n-1 cookies
    result = cookies_at_start
    return result

print(solution())