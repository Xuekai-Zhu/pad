def solution():
    
    rows = 10
    roses_per_row = 20
    red_ratio = 1/2
    white_ratio = 3/5
    pink_ratio = 1 - red_ratio - white_ratio
    total_roses = rows * roses_per_row
    red_roses = total_roses * red_ratio
    remaining_roses = total_roses - red_roses
    white_roses = remaining_roses * white_ratio
    pink_roses = remaining_roses - white_roses
    result = pink_roses
    return result

print(solution())