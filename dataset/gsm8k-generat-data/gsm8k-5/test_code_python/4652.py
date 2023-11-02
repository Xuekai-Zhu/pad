def solution():
    # Calculate the total amount of liquid Jamie has already consumed
    total_consumed = 8 + 16  # A cup of milk equals 8 ounces, a pint of grape juice equals 16 ounces

    # Calculate the maximum amount of liquid Jamie can consume before needing to use the bathroom
    max_allowed = 32 - total_consumed  # Jamie cannot have more than 32 ounces of liquid in total

    result = max_allowed
    return result

print(solution())