def solution():
    coaster_height_requirement = 54  # in inches
    marco_rubio_height = 69  # in inches
    if marco_rubio_height >= coaster_height_requirement:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())