def solution():
    """Scott has 7 pairs of shoes.  Anthony has 3 times as many pairs of shoes as Scott, and Jim has 2 less pairs than Anthony.  How many more pairs of shoes does Anthony have compared to Jim?"""
    # Define the number of pairs of shoes for Scott
    scott_shoes = 7

    # Calculate the number of pairs of shoes for Anthony
    anthony_shoes = 3 * scott_shoes

    # Calculate the number of pairs of shoes for Jim
    jim_shoes = anthony_shoes - 2

    # Calculate the difference in the number of pairs of shoes between Anthony and Jim
    difference = anthony_shoes - jim_shoes

    # Display the difference in the number of pairs of shoes between Anthony and Jim
    result = difference
    return result

print(solution())