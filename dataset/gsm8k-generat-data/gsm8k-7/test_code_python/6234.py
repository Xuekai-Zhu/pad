def solution():
    # Let x be the number of hops taken by the third frog
    x = 1

    # Calculate the number of hops taken by the second frog
    y = 2 * x

    # Calculate the number of hops taken by the first frog
    z = 4 * y

    # Calculate the total number of hops
    total_hops = x + y + z

    # Check if the total number of hops is 99
    while total_hops != 99:
        # Increment the number of hops taken by the third frog by 1
        x += 1

        # Recalculate the number of hops taken by the second and first frogs
        y = 2 * x
        z = 4 * y

        # Recalculate the total number of hops
        total_hops = x + y + z

    # Return the number of hops taken by the second frog
    result = y
    return result

print(solution())