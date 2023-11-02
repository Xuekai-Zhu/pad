def solution():
    total_rows = 20
    plants_per_row = 10
    rows_with_parsley = 3
    rows_with_rosemary = 2
    rows_with_chives = total_rows - rows_with_parsley - rows_with_rosemary
    result = rows_with_chives * plants_per_row
    return result

print(solution())