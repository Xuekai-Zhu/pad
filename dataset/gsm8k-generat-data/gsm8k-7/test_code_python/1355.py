def solution():
    shirts_per_pants = 6
    num_pants = 40

    # Calculate the total number of shirts Mr. Jones owns
    num_shirts = shirts_per_pants * num_pants

    # Calculate the total number of pieces of clothing Mr. Jones owns
    total_clothing = num_shirts + num_pants
    result = total_clothing
    return result

print(solution())