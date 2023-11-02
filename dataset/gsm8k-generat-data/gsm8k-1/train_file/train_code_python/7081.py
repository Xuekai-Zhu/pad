def solution():
    """Donna cut her pizza into 12 slices and ate half for lunch. She ate 1/3 of the remaining pizza for dinner. How many slices are left for Donna's lunch tomorrow?"""
    total_slices = 12
    slices_left_lunch = total_slices / 2
    slices_left_dinner = (total_slices - slices_left_lunch) / 3
    slices_left_lunch_tomorrow = total_slices - slices_left_lunch - slices_left_dinner
    result = slices_left_lunch_tomorrow
    return result

print(solution())