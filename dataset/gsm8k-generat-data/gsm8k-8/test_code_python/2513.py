def solution():
    # Define the initial number of chefs and waiters
    initial_chefs = 16
    initial_waiters = 16

    # Define the number of chefs and waiters who dropped out
    drop_chefs = 6
    drop_waiters = 3

    # Calculate the remaining number of chefs and waiters
    remaining_chefs = initial_chefs - drop_chefs
    remaining_waiters = initial_waiters - drop_waiters

    result = (remaining_chefs, remaining_waiters)
    return result

print(solution())