def solution():
    # Calculate how many bolts Edward needs
    bolts_needed = 40 / 5

    # Calculate how many washers Edward needs
    washers_needed = bolts_needed * 2

    # Calculate how many washers are left in the bag
    washers_left = 20 - washers_needed

    result = washers_left
    return result

print(solution())