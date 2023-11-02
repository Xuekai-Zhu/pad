def solution():
    # Calculate the number of crayons left after Kiley and Joe took some away
    initial_crayons = 48
    kiley_crayons = initial_crayons * (1/4) 
    remaining_crayons = initial_crayons - kiley_crayons 
    joe_crayons = remaining_crayons * (1/2) 
    crayons_left = remaining_crayons - joe_crayons 
    result = crayons_left
    return result

print(solution())