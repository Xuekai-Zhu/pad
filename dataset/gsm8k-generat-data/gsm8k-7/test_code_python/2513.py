def solution():
    initial_chefs = 16
    initial_waiters = 16
    dropped_chefs = 6
    dropped_waiters = 3

    # Calculate the remaining number of chefs and waiters
    remaining_chefs = initial_chefs - dropped_chefs
    remaining_waiters = initial_waiters - dropped_waiters

    result = (remaining_chefs, remaining_waiters)
    return result

print(solution())