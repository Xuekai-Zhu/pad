def solution():
    # Define the number of rows in each field
    field1_rows = 13
    field2_rows = 16

    # Define the number of corn cobs in each row
    corn_cobs_per_row = 4

    # Calculate the total number of corn cobs in each field
    field1_total = field1_rows * corn_cobs_per_row
    field2_total = field2_rows * corn_cobs_per_row

    # Calculate the total number of corn cobs grown on the farm
    total_corn_cobs = field1_total + field2_total
    result = total_corn_cobs
    return result

print(solution())