def solution():
    
    total_wood = 672
    table_wood = 12
    chair_wood = 8

    
    table_wood_use = table_wood * 24

    
    remaining_wood = total_wood - table_wood_use

    
    chair_count = remaining_wood // chair_wood

    result = chair_count
    return result

print(solution())