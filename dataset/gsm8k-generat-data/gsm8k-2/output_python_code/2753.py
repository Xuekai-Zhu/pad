def solution():
    """Emily has 7 times as many oranges as Sandra. Sandra has 3 times as many oranges as Betty. If Betty has 12 oranges, how many oranges does Emily have?"""
    betty_oranges = 12
    sandra_oranges = 3 * betty_oranges
    emily_oranges = 7 * sandra_oranges
    result = emily_oranges
    return result

print(solution())