def solution():
    """Yves and his siblings ordered pizza and asked to have it cut into 16 slices. During dinner time, they only ate one-fourth of it. The next day, Yves ate one-fourth of the remaining pizza. Then his two siblings ate 2 slices each. How many slices of pizza were left?"""
    total_slices = 16
    slices_eaten_first_day = total_slices // 4
    slices_remaining_first_day = total_slices - slices_eaten_first_day
    slices_eaten_second_day = slices_remaining_first_day // 4
    slices_remaining_second_day = slices_remaining_first_day - slices_eaten_second_day - 4
    result = slices_remaining_second_day
    return result

print(solution())