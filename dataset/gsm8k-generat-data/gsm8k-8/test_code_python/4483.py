def solution():
    # Define the number of records and their total value
    num_records = 200
    total_value = num_records * 4

    # Calculate the number of records that Bryan is interested in and their total value
    num_interesting = num_records / 2
    value_interesting = num_interesting * 6

    # Calculate the remaining number of records and their total value
    num_remaining = num_records - num_interesting
    value_remaining = num_remaining * 1

    # Calculate Bryan's total value for all the records
    bryan_total_value = value_interesting + value_remaining

    # Calculate the difference in profit between Sammy and Bryan's deals
    difference = total_value - bryan_total_value
    result = difference
    return result

print(solution())