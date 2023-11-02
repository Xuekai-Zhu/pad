def solution():
    # Calculate the total number of cookies given away
    total_given = 15 + 23 + x + 2*15  # x is the number of cookies put in the fridge

    # Calculate the total number of cookies remaining
    remaining = 256 - total_given

    # Calculate the number of cookies put in the fridge
    x = remaining - 2*15

    result = x
    return result

print(solution())