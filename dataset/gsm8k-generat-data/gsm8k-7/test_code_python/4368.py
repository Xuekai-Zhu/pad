def solution():
    total_tape = 250
    width = 20
    length = 60

    # Calculate perimeter of the field
    perimeter = 2 * (width + length)

    # Calculate amount of tape used to wrap field once
    used_tape = perimeter

    # Calculate tape left over after wrapping field once
    remaining_tape = total_tape - used_tape
    result = remaining_tape
    return result

print(solution())