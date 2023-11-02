def solution():
    """On Saturdays and Sundays, Suzanne makes french toast for the family. She and her husband each have 1 whole slice and her daughters split 1 slice. She uses a thick sliced bread that comes 12 slices per loaf. Over 52 weeks, how many loaves of bread will she need to make french toast?"""
    slices_per_weekend = 2 + 0.5 * 2  # Suzanne, her husband, and two daughters
    slices_per_year = slices_per_weekend * 52
    loaves_per_year = slices_per_year / 12  # 12 slices per loaf
    result = loaves_per_year
    return result

print(solution())