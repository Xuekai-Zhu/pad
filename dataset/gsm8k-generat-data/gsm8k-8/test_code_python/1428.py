def solution():
    # Define the number of blocks and figurines for each type of wood
    basswood_blocks = 15
    butternut_blocks = 20
    aspen_blocks = 20

    basswood_figurines = 3 * basswood_blocks
    butternut_figurines = 4 * butternut_blocks
    aspen_figurines = 2 * basswood_figurines

    # Calculate the total number of figurines
    total_figurines = basswood_figurines + butternut_figurines + aspen_figurines
    result = total_figurines
    return result

print(solution())