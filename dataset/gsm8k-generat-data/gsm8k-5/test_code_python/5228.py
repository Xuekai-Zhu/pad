def solution():
    apples_per_crate = 42  # There are 42 apples in a crate
    crates_delivered = 12  # 12 crates of apples were delivered to the factory
    rotten_apples = 4  # 4 apples were rotten and thrown away
    total_apples = apples_per_crate * crates_delivered - rotten_apples  # Total number of good apples

    # Calculate the number of boxes required to pack the apples
    boxes_required = total_apples // 10  # Each box can fit 10 apples

    result = boxes_required
    return result

print(solution())