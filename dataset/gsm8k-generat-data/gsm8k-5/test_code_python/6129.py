def solution():
    scott_shoes = 7  # Scott has 7 pairs of shoes
    anthony_shoes = 3 * scott_shoes  # Anthony has 3 times as many pairs of shoes as Scott
    jim_shoes = anthony_shoes - 2  # Jim has 2 less pairs than Anthony

    # Calculate the difference in number of shoes between Anthony and Jim
    difference = anthony_shoes - jim_shoes
    result = difference
    return result

print(solution())