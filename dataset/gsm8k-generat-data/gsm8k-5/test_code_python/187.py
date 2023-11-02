def solution():
    total_crayons = 5 * 24  # Madeline has 5 boxes with 24 crayons in each
    unused_crayons_box1 = (5/8) * 24  # 5/8 of the crayons in the first 2 boxes were not yet used
    unused_crayons_box2 = (1 - 2/3) * 24  # 1/3 of the crayons in the third and fourth boxes were used
    unused_crayons_box3 = 24 - unused_crayons_box2  # The last box was not entirely used

    # Calculate the total number of unused crayons
    total_unused_crayons = unused_crayons_box1 * 2 + unused_crayons_box2 + unused_crayons_box3
    result = total_unused_crayons
    return result

print(solution())