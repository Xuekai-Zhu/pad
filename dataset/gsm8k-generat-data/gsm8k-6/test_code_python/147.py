def solution():
    # Calculate the number of crayons Mary has left after giving some to Becky
    green_crayons_left = 5 - 3  # Mary gives out 3 green crayons
    blue_crayons_left = 8 - 1  # Mary gives out 1 blue crayon
    total_crayons_left = green_crayons_left + blue_crayons_left
    result = total_crayons_left
    return result

print(solution())