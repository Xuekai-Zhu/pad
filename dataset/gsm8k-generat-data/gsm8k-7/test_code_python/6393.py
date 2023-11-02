def solution():
    num_shirts = 18
    num_pants = 12
    num_sweaters = 17
    num_jeans = 13
    max_items_per_cycle = 15
    cycle_time = 0.75  # 45 minutes in hours

    # Calculate the total number of items that need to be washed
    total_items = num_shirts + num_pants + num_sweaters + num_jeans

    # Calculate the total number of cycles needed
    num_cycles = total_items // max_items_per_cycle
    if total_items % max_items_per_cycle != 0:
        num_cycles += 1

    # Calculate the total washing time
    total_time = num_cycles * cycle_time
    result = total_time
    return result

print(solution())