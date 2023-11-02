def solution():
    total_slices = 16
    eaten_slices = total_slices / 4  # One-fourth eaten during dinner time
    remaining_slices = total_slices - eaten_slices
    yves_slices = remaining_slices / 4  # One-fourth of the remaining pizza eaten by Yves
    siblings_slices = 2 * 2  # Two siblings ate 2 slices each
    total_eaten_slices = eaten_slices + yves_slices + siblings_slices
    remaining_slices = total_slices - total_eaten_slices
    result = remaining_slices
    return result

print(solution())