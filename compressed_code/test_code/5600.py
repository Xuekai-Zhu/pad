def solution():
    
    total_roses = 400 - 120
    white_roses = 80
    red_roses = total_roses - white_roses
    red_roses_value = 0.75
    total_red_roses_value = red_roses_value * red_roses
    half_red_roses = red_roses / 2
    half_red_roses_value = red_roses_value * half_red_roses
    result = half_red_roses_value
    return result

print(solution())