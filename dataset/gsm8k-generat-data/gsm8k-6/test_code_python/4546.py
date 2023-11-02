def solution():
    # Calculate the remaining pieces of wood after making 24 tables
    wood_used_for_tables = 24 * 12  # 12 pieces of wood are needed for each table
    wood_remaining = 672 - wood_used_for_tables
    
    # Calculate the number of chairs that can be made with the remaining wood
    chairs = wood_remaining // 8  # 8 pieces of wood are needed for each chair
    result = chairs
    return result

print(solution())