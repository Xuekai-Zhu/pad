def solution():
    # Let x be the amount of rain in the first hour
    x = 0

    # Use a loop to iterate through possible values of x until the condition is met
    while True:
        # Calculate the amount of rain in the second hour
        y = 2 * x + 7

        # Calculate the total amount of rain in the first two hours
        total = x + y

        # Check if the total is 22, if it is, break out of the loop
        if total == 22:
            break

        # If the total is not 22, increment x and repeat the loop
        x += 1

    result = x
    return result

print(solution())