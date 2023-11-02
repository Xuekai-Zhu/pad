def solution():
    loaves = 4
    slices = 15
    total_slices = loaves * slices
    people = 10
    slices_per_person = total_slices / people
    result = slices_per_person
    return result

print(solution())