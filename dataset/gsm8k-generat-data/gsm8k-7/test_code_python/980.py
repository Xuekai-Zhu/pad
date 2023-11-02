def solution():
    field1_rows = 13
    field2_rows = 16
    corn_cobs_per_row = 4

    # Calculate the total number of corn cobs in the first field
    field1_corn_cobs = field1_rows * corn_cobs_per_row

    # Calculate the total number of corn cobs in the second field
    field2_corn_cobs = field2_rows * corn_cobs_per_row

    # Calculate the total number of corn cobs grown by the farm
    total_corn_cobs = field1_corn_cobs + field2_corn_cobs
    result = total_corn_cobs
    return result

print(solution())