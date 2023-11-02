def solution():
    apples_per_crate = 180  # Each crate contained 180 apples
    crates_delivered = 12  # 12 crates were delivered
    total_apples = apples_per_crate * crates_delivered  # Total number of apples delivered
    rotten_apples = 160  # 160 apples were found to be rotten
    good_apples = total_apples - rotten_apples  # Number of good apples remaining
    apples_per_box = 20  # Each box contains 20 apples

    # Calculate the number of boxes of apples
    boxes_of_apples = good_apples / apples_per_box
    result = boxes_of_apples
    return result

print(solution())