def solution():
    # pyramid is four levels tall
    num_levels = 4
    
    # initialize case count to 1 for the top level
    case_count = 1
    
    # iterate over the levels, adding 4 cases for each level
    for i in range(num_levels):
        case_count = case_count + 4
    
    # return the total case count
    return case_count

print(solution())