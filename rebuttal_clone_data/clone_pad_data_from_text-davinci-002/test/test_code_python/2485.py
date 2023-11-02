def solution():
    tape = 250
    field_width = 20
    field_length = 60
    perimeter = 2 * (field_width + field_length)
    tape_leftover = tape - perimeter
    result = tape_leftover
    return result

print(solution())