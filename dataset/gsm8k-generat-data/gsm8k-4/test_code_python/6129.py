def solution():
    """Scott has 7 pairs of shoes. Anthony has 3 times as many pairs of shoes as Scott, and Jim has 2 less pairs than Anthony. How many more pairs of shoes does Anthony have compared to Jim?"""
    # Define the number of shoes Scott has
    scott_shoes = 7

    # Calculate the number of shoes Anthony has
    anthony_shoes = scott_shoes * 3

    # Calculate the number of shoes Jim has
    jim_shoes = anthony_shoes - 2

    # Calculate the difference in the number of shoes between Anthony and Jim
    difference = anthony_shoes - jim_shoes

    # return the result
    result = difference
    return result

print(solution())