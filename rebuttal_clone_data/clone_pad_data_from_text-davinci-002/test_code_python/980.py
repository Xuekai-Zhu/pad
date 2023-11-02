def solution():
    field1_rows = 13
    field2_rows = 16
    cobs_per_row = 4
    field1_cobs = field1_rows * cobs_per_row
    field2_cobs = field2_rows * cobs_per_row
    total_cobs = field1_cobs + field2_cobs
    result = total_cobs
    return result

print(solution())