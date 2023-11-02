def solution():
    num_red_crayons = 14

    # Calculate the number of blue crayons
    num_blue_crayons = num_red_crayons + 5

    # Calculate the double of the number of blue crayons
    double_num_blue_crayons = num_blue_crayons * 2

    # Calculate the number of yellow crayons
    num_yellow_crayons = double_num_blue_crayons - 6

    result = num_yellow_crayons
    return result

print(solution())