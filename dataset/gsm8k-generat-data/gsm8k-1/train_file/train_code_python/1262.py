def solution():
    """Phil has a coin collection he likes to add to. He started with 50 state quarters his parents gave him. Over the next year he doubled this. The following year he collected 3 each month. The year after that he collected 1 every third month. The year after that he lost a quarter of them when he misplaced his collection. How many did he have left after losing some?"""
    start_quarters = 50
    doubled_quarters = start_quarters * 2
    third_year_quarters = 3 * 12
    fourth_year_quarters = (12 // 3) + 1 # Every third month + 1 extra
    total_quarters = doubled_quarters + third_year_quarters + fourth_year_quarters
    lost_quarters = total_quarters // 4
    remaining_quarters = total_quarters - lost_quarters
    result = remaining_quarters
    return result

print(solution())