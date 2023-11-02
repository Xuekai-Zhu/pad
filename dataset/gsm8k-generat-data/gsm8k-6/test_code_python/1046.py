def solution():
    # Calculate the total number of roses in the bouquet
    total_roses = 3 * 12  # 1 dozen equals 12

    # Calculate the number of roses Susan gave to her daughter
    daughter_roses = total_roses / 2

    # Calculate the number of roses left in the vase
    remaining_roses = total_roses - daughter_roses

    # Calculate the number of wilted roses
    wilted_roses = remaining_roses / 3

    # Calculate the number of remaining roses after removing the wilted ones
    final_roses = remaining_roses - wilted_roses
    result = final_roses
    return result

print(solution())