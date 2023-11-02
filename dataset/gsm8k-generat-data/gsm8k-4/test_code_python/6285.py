def solution():
    """Maggie went to Lou's aquarium and saw 100 goldfish in the aquarium. She asked if she could take some home to care for, and she was allowed to catch half of them. While using a catching net, she caught 3/5 of the total number of goldfish she was allowed to take home. How many goldfish does Maggie remain with to catch to get the total number she was allowed to take home?"""
    # Define the initial number of goldfish and the fraction Maggie is allowed to take
    initial_goldfish = 100
    fraction_allowed = 0.5

    # Calculate the number of goldfish Maggie is allowed to take
    allowed_goldfish = initial_goldfish * fraction_allowed

    # Calculate the number of goldfish Maggie caught
    caught_goldfish = allowed_goldfish * 3/5

    # Calculate the number of goldfish Maggie still needs to catch
    remaining_goldfish = allowed_goldfish - caught_goldfish

    result = remaining_goldfish
    return result

print(solution())