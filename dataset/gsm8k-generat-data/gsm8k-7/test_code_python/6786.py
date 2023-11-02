def solution():
    record_length = 26
    starting_length = 2
    growth_rate = 0.1
    age = 12

    # Calculate the time it will take for Sandy to reach the record length
    time_to_record = (record_length - starting_length) / growth_rate

    # Add the time it will take to her current age to find her age when she achieves the record
    age_at_record = age + time_to_record
    result = age_at_record
    return result

print(solution())