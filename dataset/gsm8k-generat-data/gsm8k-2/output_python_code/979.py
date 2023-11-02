def solution():
    """A farm is growing corn in 2 fields. One of the fields has 13 full rows of corn cobs, and the other field has 16 full rows of corn cobs. If each row contains 4 corn cobs, how many corn cobs has the farm grown?"""
    field1_rows = 13
    field2_rows = 16
    corn_cobs_per_row = 4
    total_corn_cobs = (field1_rows + field2_rows) * corn_cobs_per_row
    result = total_corn_cobs
    return result

print(solution())