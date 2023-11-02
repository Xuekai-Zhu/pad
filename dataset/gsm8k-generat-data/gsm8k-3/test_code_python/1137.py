def solution():
    """James has 7 more than 4 times the number of Oreos Jordan has.  If there are 52 Oreos total, how many does James have?"""
    # Define the total number of Oreos and the number of Oreos Jordan has
    total_oreos = 52
    jordan_oreos = total_oreos / 5

    # Calculate the number of Oreos James has
    james_oreos = 4 * jordan_oreos + 7

    # Display the number of Oreos James has
    result = james_oreos
    return result

print(solution())