def solution():
    """The cafe has 16 chefs and 16 waiters. If 6 chefs and 3 waiters drop out, how many chefs and waiters are left?"""
    # Define the initial number of chefs and waiters
    initial_chefs = 16
    initial_waiters = 16

    # Define the number of chefs and waiters who dropped out
    dropped_chefs = 6
    dropped_waiters = 3

    # Calculate the final number of chefs and waiters
    final_chefs = initial_chefs - dropped_chefs
    final_waiters = initial_waiters - dropped_waiters

    # return the result
    result = (final_chefs, final_waiters)
    return result

print(solution())