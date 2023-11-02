def solution():
    # Calculate the total number of chairs in indoor tables
    chairs_indoor = 9 * 10  # 9 indoor tables, each with 10 chairs

    # Calculate the total number of chairs in outdoor tables
    chairs_outdoor = 11 * 3  # 11 outdoor tables, each with 3 chairs

    # Calculate the total number of chairs in the cafe
    total_chairs = chairs_indoor + chairs_outdoor
    result = total_chairs
    return result

print(solution())