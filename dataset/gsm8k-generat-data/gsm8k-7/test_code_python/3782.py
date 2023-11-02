def solution():
    num_sand_dollars = 10

    # Calculate the number of pieces of glass in the jar
    num_pieces_of_glass = num_sand_dollars * 3

    # Calculate the number of seashells in the bucket
    num_seashells = num_pieces_of_glass * 5

    # Calculate the total number of treasures Simon collected
    total_treasures = num_sand_dollars + num_pieces_of_glass + num_seashells
    result = total_treasures
    return result

print(solution())