def solution():
    # Calculate the number of red crayons in the box
    red_crayons = 4 * 3  # there are four times as many red crayons as blue crayons, and there are 3 blue crayons
    total_crayons = red_crayons + 3  # add the number of blue crayons to the number of red crayons
    result = total_crayons
    return result

print(solution())