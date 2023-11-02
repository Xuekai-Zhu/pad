def solution():
    # Original number of chefs and waiters
    num_chefs = 16
    num_waiters = 16

    # Number of chefs and waiters who dropped out
    dropped_chefs = 6
    dropped_waiters = 3

    # Calculate the number of chefs and waiters left
    remaining_chefs = num_chefs - dropped_chefs
    remaining_waiters = num_waiters - dropped_waiters

    result = f"There are {remaining_chefs} chefs and {remaining_waiters} waiters left."
    return result

print(solution())