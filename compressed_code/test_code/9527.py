def solution():
    
    total_nails = 20
    purple_nails = 6
    blue_nails = 8
    striped_nails = total_nails - purple_nails - blue_nails
    percent_blue = (blue_nails / total_nails) * 100
    percent_striped = (striped_nails / total_nails) * 100
    difference = abs(percent_blue - percent_striped)
    result = difference
    return result

print(solution())