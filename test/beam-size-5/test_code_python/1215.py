def solution():
    num_wooden_tables = 4
    wooden_table_price = 20

    num_roof_frames = 2
    roof_frame_price = 10

    # Calculate the total cost of all wooden tables
    total_wooden_cost = num_wooden_tables * wooden_table_price

    # Calculate the total cost of all roof frames
    total_roof_frames_cost = num_roof_frames * roof_frame_price

    # Calculate the total cost of all items
    total_cost = total_wooden_cost + total_roof_frames_cost
    result = total_cost
    return result

print(solution())