def solution():
    """Michelle had some leftover cans of silly string from her birthday party. She split them among Roger and 3 of his friends. Then Roger decided to give 2 of his cans to his brothers so that he now has 4 for himself. How many cans of silly string did Michelle have to start with?"""
    # Define the number of friends
    num_friends = 3

    # Define the number of cans Roger has after giving 2 to his brothers
    roger_cans = 4

    # Calculate the total number of cans after Roger gave 2 to his brothers
    total_cans = roger_cans + 2

    # Calculate the number of cans split between Roger and his friends
    split_cans = total_cans * (num_friends + 1)

    # Calculate the total number of cans Michelle had
    michelle_cans = split_cans

    result = michelle_cans
    return result

print(solution())