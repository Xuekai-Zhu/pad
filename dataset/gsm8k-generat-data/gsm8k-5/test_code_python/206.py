def solution():
    lions = 0  # Initialize the number of lions at first
    for i in range(12):  # Iterate over 12 months
        lions = lions + 5 - 1  # Add 5 lion cubs and subtract 1 dead lion every month
    initial_lions = 148 - lions  # Calculate the initial number of lions
    result = initial_lions
    return result

print(solution())