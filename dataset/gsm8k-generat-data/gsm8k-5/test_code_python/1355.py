def solution():
    shirts_per_pants = 6  # Mr. Jones has 6 shirts for every pair of pants
    num_pants = 40  # Mr. Jones has 40 pants

    # Calculate the total number of shirts Mr. Jones has
    num_shirts = shirts_per_pants * num_pants

    # Calculate the total number of pieces of clothes Mr. Jones owns
    total_clothes = num_shirts + num_pants
    result = total_clothes
    return result

print(solution())