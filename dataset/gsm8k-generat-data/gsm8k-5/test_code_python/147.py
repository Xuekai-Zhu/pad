def solution():
    initial_green_crayons = 5  # Mary has 5 green crayons initially
    initial_blue_crayons = 8  # Mary has 8 blue crayons initially
    given_green_crayons = 3  # Mary gives 3 green crayons to Becky
    given_blue_crayons = 1  # Mary gives 1 blue crayon to Becky
    
    # Calculate the number of green and blue crayons Mary has left
    remaining_green_crayons = initial_green_crayons - given_green_crayons
    remaining_blue_crayons = initial_blue_crayons - given_blue_crayons
    
    # Calculate the total number of crayons Mary has left
    total_remaining_crayons = remaining_green_crayons + remaining_blue_crayons
    result = total_remaining_crayons
    return result

print(solution())