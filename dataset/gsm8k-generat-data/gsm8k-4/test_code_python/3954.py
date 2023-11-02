def solution():
    """Jesse is playing with a pile of building blocks. He first builds a building with 80 building blocks. Then he builds a farmhouse with 123 building blocks. He adds a fenced-in area next to the farm made of 57 building blocks. If Jesse has 84 building blocks left, how many building blocks did he start with?"""
    # Define the number of building blocks Jesse started with
    blocks_start = None

    # Calculate the total number of building blocks used
    blocks_used = 80 + 123 + 57

    # Calculate the number of building blocks left
    blocks_left = 84

    # Calculate the number of building blocks Jesse started with
    blocks_start = blocks_used + blocks_left

    # return the result
    result = blocks_start
    return result

print(solution())