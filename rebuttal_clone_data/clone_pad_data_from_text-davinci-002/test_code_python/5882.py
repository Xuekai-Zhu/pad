def solution():
    people = 4
    weeks = 52
    slices_per_loaf = 12
    slices_needed_per_weekend = people * 2
    loaves_needed_per_weekend = slices_needed_per_weekend / slices_per_loaf
    total_loaves_needed = loaves_needed_per_weekend * weeks
    result = total_loaves_needed
    return result

print(solution())