def solution():
    total_slices = 12
    slices_eaten_lunch = total_slices / 2
    slices_eaten_dinner = (total_slices - slices_eaten_lunch) / 3
    slices_left = total_slices - (slices_eaten_lunch + slices_eaten_dinner)
    result = slices_left
    return result

print(solution())