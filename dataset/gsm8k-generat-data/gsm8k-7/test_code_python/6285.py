def solution():
    num_goldfish = 100
    catch_percentage = 0.5  # Maggie was allowed to catch half of the goldfish
    caught_percentage = 0.6  # Maggie caught 3/5 of the goldfish she was allowed to take home

    # Calculate the total number of goldfish Maggie was allowed to take home
    num_allowed = num_goldfish * catch_percentage

    # Calculate the number of goldfish Maggie caught
    num_caught = num_allowed * caught_percentage

    # Calculate the number of goldfish Maggie still needs to catch to reach the total allowed
    num_remaining = num_allowed - num_caught
    result = num_remaining
    return result

print(solution())