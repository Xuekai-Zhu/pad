def solution():
    chinese_zodiac_animals = ["dog", "pig"]
    chordata_animals = ["pig"]
    overlap = [animal for animal in chinese_zodiac_animals if animal in chordata_animals]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())