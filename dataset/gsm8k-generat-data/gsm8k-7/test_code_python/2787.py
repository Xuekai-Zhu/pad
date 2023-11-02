def solution():
    bottle_size = 20
    refills_per_day = 3
    spilled_ounces = 5 + 8
    days = 7

    # Calculate the total number of refills Remi does in a week
    total_refills = refills_per_day * days

    # Calculate the total amount of water Remi drinks before spills
    total_drunk = (bottle_size - spilled_ounces) * total_refills

    result = total_drunk
    return result

print(solution())