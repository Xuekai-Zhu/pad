def solution():
    va_general_assembly_seats = 140
    swiss_guard_members = 135
    if swiss_guard_members >= va_general_assembly_seats:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())