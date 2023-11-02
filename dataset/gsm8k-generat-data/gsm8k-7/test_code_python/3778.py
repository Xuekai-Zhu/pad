def solution():
    current_length = 200
    target_length = 650
    built_first_day = 50
    built_second_day = 3 * built_first_day

    # Calculate the total length of highway built after the second day
    total_built = current_length + built_first_day + built_second_day

    # Calculate the remaining length to be built to reach the target length
    remaining_length = target_length - total_built
    result = remaining_length
    return result

print(solution())