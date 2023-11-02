def solution():
    # Calculate the total number of times Sarah saw her reflection
    tall_count_Sarah = 10 * 3 * 2  # 3 times each, 2 mirrors in each room
    wide_count_Sarah = 5 * 5 * 2  # 5 times each, 2 mirrors in each room
    total_count_Sarah = tall_count_Sarah + wide_count_Sarah

    # Calculate the total number of times Ellie saw her reflection
    tall_count_Ellie = 6 * 3 * 2  # 3 times each, 2 mirrors in each room
    wide_count_Ellie = 3 * 5 * 2  # 5 times each, 2 mirrors in each room
    total_count_Ellie = tall_count_Ellie + wide_count_Ellie

    # Calculate the total number of times both Sarah and Ellie
    total_count = total_count_Sarah + total_count_Ellie
    result = total_count
    return result

print(solution())