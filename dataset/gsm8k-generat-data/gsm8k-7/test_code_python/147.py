def solution():
    num_green_crayons = 5
    num_blue_crayons = 8

    # Give 3 green and 1 blue crayon to Becky
    num_green_crayons -= 3
    num_blue_crayons -= 1

    # Calculate the total number of crayons Mary has left
    total_crayons_left = num_green_crayons + num_blue_crayons
    result = total_crayons_left
    return result

print(solution())