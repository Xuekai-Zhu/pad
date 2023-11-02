def solution():
    """A house’s living room, dining room and kitchen take up 1,000 sq ft. The house also has a guest bedroom and a master bedroom suite. If the guest bedroom is a quarter of the size of the master bedroom suite, and the house is 2,300 sq ft total, how large is the master bedroom suite?"""
    # Define the size of the living room, dining room and kitchen
    ldk_size = 1000

    # Calculate the remaining size of the house
    remaining_size = 2300 - ldk_size

    # Calculate the total size of the guest bedroom and master bedroom suite
    bedrooms_size = remaining_size / 5

    # Calculate the size of the master bedroom suite
    master_size = bedrooms_size * 4

    # Return the result
    result = master_size
    return result

print(solution())