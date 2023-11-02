def solution():
    num_wood = 672
    num_table_wood = 12
    num_chair_wood = 8
    num_tables = 24

    # Calculate the total wood used for tables
    total_table_wood = num_tables * num_table_wood

    # Calculate the remaining wood available for chairs
    remaining_wood = num_wood - total_table_wood

    # Calculate the maximum number of chairs that can be made with the remaining wood
    num_chairs = remaining_wood // num_chair_wood
    result = num_chairs
    return result

print(solution())