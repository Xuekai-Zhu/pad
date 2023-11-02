def solution():
    hydrogen_atomic_number = 1
    spice_girls_members = 5
    hydrogen_squared = hydrogen_atomic_number ** 2
    if hydrogen_squared > spice_girls_members:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())