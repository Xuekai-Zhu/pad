def solution():
    slices_per_bread = 12  # A loaf of bread has 12 slices
    total_slices_per_weekend = (1 + 1 + 0.5 + 0.5) * 2  # Suzanne, her husband, and two daughters each eat french toast on Saturday and Sunday
    loaves_per_weekend = total_slices_per_weekend / slices_per_bread  # Calculate the number of loaves needed per weekend
    loaves_per_year = loaves_per_weekend * 52  # Calculate the number of loaves needed per year
    result = loaves_per_year
    return result

print(solution())