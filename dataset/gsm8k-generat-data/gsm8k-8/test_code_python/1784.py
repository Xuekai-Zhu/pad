def solution():
    total_chips = 22
    given_to_brother = 7
    given_to_sister = 5

    remaining_chips = total_chips - given_to_brother - given_to_sister
    result = remaining_chips
    return result

print(solution())