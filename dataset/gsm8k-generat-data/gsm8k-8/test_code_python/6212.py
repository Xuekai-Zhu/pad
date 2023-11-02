def solution():
    # Define the initial number of bears and the number taken out
    initial_bears = 20
    favorite_bears = 8

    # Calculate the number of bears remaining
    remaining_bears = initial_bears - favorite_bears

    # Calculate the number of bears each sister received
    sister_bears = remaining_bears / 3

    # Calculate the total number of bears Eden has now
    eden_bears = sister_bears + 10

    result = eden_bears
    return result

print(solution())