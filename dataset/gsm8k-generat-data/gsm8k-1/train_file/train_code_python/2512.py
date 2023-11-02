def solution():
    """The cafe has 16 chefs and 16 waiters. If 6 chefs and 3 waiters drop out, how many chefs and waiters are left?"""
    initial_chefs = 16
    initial_waiters = 16
    lost_chefs = 6
    lost_waiters = 3
    remaining_chefs = initial_chefs - lost_chefs
    remaining_waiters = initial_waiters - lost_waiters
    result = (remaining_chefs, remaining_waiters)
    return result

print(solution())