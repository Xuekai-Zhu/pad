def solution():
    # Calculate the number of pieces of glass in the jar
    num_glass = 10 * 3

    # Calculate the number of seashells in the bucket
    num_seashells = num_glass * 5

    # Calculate the total number of treasures collected
    total_treasures = num_glass + num_seashells + 10
    result = total_treasures
    return result

print(solution())