def solution():
    # Calculate the total number of apples delivered to the factory
    total_apples = 42 * 12  # 12 crates of apples, each crate has 42 apples

    # Calculate the number of apples that were thrown away
    rotten_apples = 4

    # Calculate the number of apples that were packed into boxes
    remaining_apples = total_apples - rotten_apples
    boxes_of_apples = remaining_apples // 10  # 10 apples can fit into one box

    result = boxes_of_apples
    return result

print(solution())