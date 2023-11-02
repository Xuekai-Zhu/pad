def solution():
    initial_biscuits = 32
    father_gift = 13
    mother_gift = 15
    brother_shared = 20

    # Calculate the total number of biscuits Randy has
    total_biscuits = initial_biscuits + father_gift + mother_gift - brother_shared

    result = total_biscuits
    return result

print(solution())