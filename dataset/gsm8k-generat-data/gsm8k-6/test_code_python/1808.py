def solution():
    # Calculate the total number of zits in Ms. Swanson's class and Mr. Jones' class
    total_zits_swanson = 25 * 5  # 25 kids with an average of 5 zits each
    total_zits_jones = 32 * 6  # 32 kids with an average of 6 zits each

    # Calculate the difference in the total number of zits between the two classes
    difference_zits = total_zits_jones - total_zits_swanson
    result = difference_zits
    return result

print(solution())