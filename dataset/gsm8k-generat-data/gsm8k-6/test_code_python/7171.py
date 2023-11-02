def solution():
    # Calculate the total number of crayons produced by the factory in 4 hours
    crayons_per_box = 2 * 4  # 2 crayons of each color in each box
    crayons_per_hour = crayons_per_box * 4  # enough crayons to fill 5 boxes per hour
    crayons_in_4_hours = crayons_per_hour * 4
    result = crayons_in_4_hours
    return result

print(solution())