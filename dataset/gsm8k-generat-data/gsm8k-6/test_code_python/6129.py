def solution():
    # Calculate the number of shoes Scott has
    scott_shoes = 7
    
    # Calculate the number of shoes Anthony has
    anthony_shoes = 3 * scott_shoes
    
    # Calculate the number of shoes Jim has
    jim_shoes = anthony_shoes - 2
    
    # Calculate the difference in number of shoes between Anthony and Jim
    diff_shoes = anthony_shoes - jim_shoes
    result = diff_shoes
    return result

print(solution())