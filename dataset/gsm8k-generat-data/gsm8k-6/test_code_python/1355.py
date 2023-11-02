def solution():
    # Calculate the total number of shirts Mr. Jones has
    total_shirts = 6 * 40  # Mr. Jones has 6 shirts for every pair of pants, and he has 40 pants

    # Calculate the total number of pieces of clothes Mr. Jones owns
    total_clothes = total_shirts + 40  # all other factors remain the same, so we just need to add the number of pants to the total shirts
    result = total_clothes
    return result

print(solution())