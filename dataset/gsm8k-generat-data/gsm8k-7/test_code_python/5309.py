def solution():
    recess_breaks_per_day = 2
    recess_break_length = 15
    lunch_break_length = 30
    additional_recess_length = 20

    # Calculate the total length of recess breaks
    total_recess_length = recess_breaks_per_day * recess_break_length

    # Calculate the total length of all breaks
    total_break_length = total_recess_length + lunch_break_length + additional_recess_length

    result = total_break_length
    return result

print(solution())