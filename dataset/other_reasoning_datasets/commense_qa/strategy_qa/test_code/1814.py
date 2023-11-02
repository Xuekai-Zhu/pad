def solution():
    northern_hemisphere_solstice_month = "December"
    southern_hemisphere_solstice_month = "June"
    months_before_northern_solstice = ord(northern_hemisphere_solstice_month) - ord('A') + 1
    months_before_southern_solstice = ord(southern_hemisphere_solstice_month) - ord('A') + 1
    if months_before_northern_solstice < months_before_southern_solstice - 6:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())