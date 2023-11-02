def solution():
    # Calculate the total number of chairs for indoor tables
    chairs_indoor = 8 * 3  # 8 indoor tables, each with 3 chairs

    # Calculate the total number of chairs for outdoor tables
    chairs_outdoor = 12 * 3  # 12 outdoor tables, each with 3 chairs

    # Calculate the total number of chairs in the bakery
    total_chairs = chairs_indoor + chairs_outdoor
    result = total_chairs
    return result

print(solution())