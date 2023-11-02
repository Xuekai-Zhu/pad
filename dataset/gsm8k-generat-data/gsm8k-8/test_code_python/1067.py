def solution():
    # Define the number of crates and apples per crate
    num_crates = 12
    apples_per_crate = 180

    # Calculate the total number of apples
    total_apples = num_crates * apples_per_crate

    # Subtract the number of rotten apples
    good_apples = total_apples - 160

    # Calculate the number of boxes
    boxes = good_apples // 20

    result = boxes
    return result

print(solution())