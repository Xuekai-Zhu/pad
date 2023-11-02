def solution():
    
    total_rows = 10
    roses_per_row = 20
    red_percent = 0.5
    white_percent = 0.6
    red_roses = total_rows * roses_per_row * red_percent
    remaining_roses = total_rows * roses_per_row - red_roses
    white_roses = remaining_roses * white_percent
    pink_roses = remaining_roses - white_roses
    result = pink_roses
    return result

print(solution())