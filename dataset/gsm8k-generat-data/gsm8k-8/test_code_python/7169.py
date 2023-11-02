def solution():
    # Define the number of pints Annie picked
    annie_pints = 8

    # Calculate the number of pints Kathryn picked
    kathryn_pints = annie_pints + 2

    # Calculate the number of pints Ben picked
    ben_pints = kathryn_pints - 3

    # Calculate the total number of pints picked
    total_pints = annie_pints + kathryn_pints + ben_pints
    result = total_pints
    return result

print(solution())