def solution():
    """James has 7 more than 4 times the number of Oreos Jordan has. If there are 52 Oreos total, how many does James have?"""
    # Define the total number of Oreos and the number of Oreos Jordan has
    total_oreos = 52
    jordan_oreos = None

    # Calculate the number of Oreos James has
    james_oreos = 4 * jordan_oreos + 7

    # Use the fact that the total number of Oreos is the sum of Oreos Jordan and Oreos James have
    jordan_oreos = (total_oreos - james_oreos) / 5

    result = james_oreos
    return result

print(solution())