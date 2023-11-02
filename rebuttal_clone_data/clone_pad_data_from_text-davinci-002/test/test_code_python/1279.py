def solution():
    children = 11
    adults = 20
    child_clothes = 4
    adult_clothes = 3
    clotheslines_per_house = 2
    total_clotheslines = children + adults
    total_clothes = children * child_clothes + adults * adult_clothes
    clotheslines_needed = total_clothes / 2
    houses = clotheslines_needed / clotheslines_per_house
    result = houses
    return result

print(solution())