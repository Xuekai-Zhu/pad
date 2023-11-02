def solution():
    pencils_bought = 20  # Autumn had 20 pencils at the start of the school year
    pencils_misplaced = 7  # Autumn misplaced 7 pencils in the first month
    pencils_broken = 3  # Autumn broke 3 pencils in the first month
    pencils_found = 4  # Autumn found 4 misplaced pencils in the first month
    pencils_bought_new = 2  # Autumn bought 2 new pencils in the first month

    # Calculate the total number of pencils Autumn has after the first month
    total_pencils = pencils_bought - pencils_misplaced - pencils_broken + pencils_found + pencils_bought_new
    result = total_pencils
    return result

print(solution())