def solution():
    total_goldfish = 100
    goldfish_allowed = total_goldfish / 2  # Maggie is allowed to take half of the goldfish

    # Maggie caught 3/5 of the goldfish she was allowed to take home
    goldfish_caught = goldfish_allowed * 3 / 5

    # Calculate how many goldfish Maggie still needs to catch
    goldfish_remaining = goldfish_allowed - goldfish_caught
    result = goldfish_remaining
    return result

print(solution())