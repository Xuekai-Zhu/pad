def solution():
    
    total_nails = 20
    purple_nails = 6
    blue_nails = 8
    striped_nails = total_nails - purple_nails - blue_nails
    blue_percent = (blue_nails / total_nails) * 100
    striped_percent = (striped_nails / total_nails) * 100
    difference = blue_percent - striped_percent
    result = difference
    return result

print(solution())