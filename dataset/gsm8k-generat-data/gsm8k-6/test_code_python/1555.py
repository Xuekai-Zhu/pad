def solution():
    # Calculate the number of silver and bronze stickers that Miss Walter has
    silver_stickers = 2 * 50  # twice as many silver stickers as gold stickers
    bronze_stickers = silver_stickers - 20  # 20 fewer bronze stickers than silver stickers
    
    # Calculate the total number of stickers that Miss Walter has
    total_stickers = 50 + silver_stickers + bronze_stickers
    
    # Calculate the number of stickers each student will receive
    stickers_per_student = total_stickers // 5  # integer division

    result = stickers_per_student
    return result

print(solution())