def solution():
    """James has 3 more than 2 times the number of Oreos Jordan has. If there are 36 Oreos total, how many does Jordan have?"""
    # Define the total number of Oreos
    total_oreos = 36

    # Define the number of Oreos Jordan has
    jordan_oreos = None

    # Calculate the number of Oreos James has
    james_oreos = 2 * jordan_oreos + 3

    # Use the total and the sum of Jordan and James' Oreos to solve for Jordan's Oreos
    jordan_oreos = (total_oreos - james_oreos)

    # return the result
    result = jordan_oreos
    return result

print(solution())