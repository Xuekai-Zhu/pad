def solution():
    # Calculate the length of fencing around the garden
    garden_fencing = 2 * (12 + 9)  # fencing around the garden is twice the length of sum of length and breadth

    # Calculate the length of fencing around the playground
    playground_fencing = 4 * 27  # fencing around the square playground is four times the length of one side

    # Calculate the total length of fencing
    total_fencing = garden_fencing + playground_fencing
    result = total_fencing
    return result

print(solution())