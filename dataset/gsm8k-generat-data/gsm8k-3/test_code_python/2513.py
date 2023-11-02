def solution():
    """The cafe has 16 chefs and 16 waiters. If 6 chefs and 3 waiters drop out, how many chefs and waiters are left?"""
    # Define the initial number of chefs and waiters
    initial_chefs = 16
    initial_waiters = 16

    # Define the number of chefs and waiters who drop out
    dropped_chefs = 6
    dropped_waiters = 3

    # Calculate the remaining number of chefs and waiters
    remaining_chefs = initial_chefs - dropped_chefs
    remaining_waiters = initial_waiters - dropped_waiters

    # Display the remaining number of chefs and waiters
    result = (remaining_chefs, remaining_waiters)
    return result

print(solution())