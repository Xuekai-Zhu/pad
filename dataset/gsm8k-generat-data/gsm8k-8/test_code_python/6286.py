def solution():
    # Define the initial number of bees
    initial_bees = 12500

    # Define the daily change in bee population
    bee_change = 3000 - 900

    # Calculate the total number of bees after 7 days
    total_bees = initial_bees + (7 * bee_change)
    result = total_bees
    return result

print(solution())