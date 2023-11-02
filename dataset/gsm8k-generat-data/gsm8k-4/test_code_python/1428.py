def solution():
    """Adam owns a wood carving shop, if a block of basswood can create 3 figurines and a block of butternut wood can create 4 figurines, and a block of Aspen wood can make twice the amount of figurines compared to basswood, how many figurines can he make if he owns 15 blocks of basswood, 20 blocks of butternut wood, and 20 blocks of Aspen wood?"""
    # Define the number of blocks of each type of wood
    basswood_blocks = 15
    butternut_blocks = 20
    aspen_blocks = 20

    # Calculate the total number of figurines that can be made from each type of wood
    basswood_figurines = 3 * basswood_blocks
    butternut_figurines = 4 * butternut_blocks
    aspen_figurines = 2 * basswood_figurines

    # Calculate the total number of figurines that can be made
    total_figurines = basswood_figurines + butternut_figurines + aspen_figurines

    # return the result
    result = total_figurines
    return result

print(solution())