def solution():
    """A farm is growing corn in 2 fields. One of the fields has 13 full rows of corn cobs, and the other field has 16 full rows of corn cobs. If each row contains 4 corn cobs, how many corn cobs has the farm grown?"""
    # Define the number of rows in each field
    rows_field1 = 13
    rows_field2 = 16

    # Define the number of corn cobs per row
    corn_cobs_per_row = 4

    # Calculate the total number of corn cobs
    total_corn_cobs = (rows_field1 + rows_field2) * corn_cobs_per_row

    # return the result
    result = total_corn_cobs
    return result

print(solution())