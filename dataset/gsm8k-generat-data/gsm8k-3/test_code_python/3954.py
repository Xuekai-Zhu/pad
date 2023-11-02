def solution():
    """Jesse is playing with a pile of building blocks. He first builds a building with 80 building blocks. Then he builds a farmhouse with 123 building blocks. He adds a fenced-in area next to the farm made of 57 building blocks. If Jesse has 84 building blocks left, how many building blocks did he start with?"""
    # Calculate the total number of building blocks used
    total_blocks_used = 80 + 123 + 57

    # Calculate the number of building blocks Jesse started with
    starting_blocks = total_blocks_used + 84

    # Display the number of building blocks Jesse started with
    result = starting_blocks
    return result

print(solution())