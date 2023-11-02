def solution():
    """Andy had a platter of chocolate cookies. He ate 3 of them then gave his little brother 5 because he was behaving. He then handed the platter to his basketball team of eight members. The first player to arrive took 1, the second player to arrive took 3, the third player took 5, and so on. When the last player took his share, the platter was empty. How many chocolate cookies did Andy have from start with?"""
    initial_cookies = 0
    eaten_cookies = 3
    given_cookies = 5
    for i in range(1, 9):
        if i % 2 == 1:
            initial_cookies += i
        else:
            initial_cookies -= i

    total_cookies = initial_cookies - eaten_cookies - given_cookies
    result = total_cookies
    return result

print(solution())