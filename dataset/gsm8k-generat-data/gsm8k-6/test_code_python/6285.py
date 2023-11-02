def solution():
    # Find the number of goldfish Maggie was allowed to take home
    allowed_goldfish = 100 / 2  # Maggie was allowed to take half of the goldfish in the aquarium
    caught_goldfish = (3/5) * allowed_goldfish  # Maggie caught 3/5 of the allowed goldfish
    remaining_goldfish = allowed_goldfish - caught_goldfish  # find the remaining goldfish to catch
    result = remaining_goldfish
    return result

print(solution())