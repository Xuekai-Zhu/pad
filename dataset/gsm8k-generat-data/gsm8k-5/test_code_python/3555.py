def solution():
    weeks = 4  # There are 4 weeks in a month

    # Calculate the total number of pens Alex will have after a month
    total_pens = 4 * (2 ** (weeks-1))

    # Calculate the number of pens Jane will have after a month
    jane_pens = 16

    # Calculate the difference in pens between Alex and Jane
    difference = total_pens - jane_pens
    result = difference
    return result

print(solution())