def solution():
    """A farm is growing corn in 2 fields. One of the fields has 13 full rows of corn cobs, and the other field has 16 full rows of corn cobs. If each row contains 4 corn cobs, how many corn cobs has the farm grown?"""
    # Define the number of rows and corn cobs per row
    ROWS_FIELD1 = 13
    ROWS_FIELD2 = 16
    CORN_COBS_PER_ROW = 4

    # Calculate the total number of corn cobs in each field
    total_corn_cobs_field1 = ROWS_FIELD1 * CORN_COBS_PER_ROW
    total_corn_cobs_field2 = ROWS_FIELD2 * CORN_COBS_PER_ROW

    # Calculate the total number of corn cobs grown by the farm
    total_corn_cobs = total_corn_cobs_field1 + total_corn_cobs_field2

    # Display the total number of corn cobs
    result = total_corn_cobs
    return result

print(solution())