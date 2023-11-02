def solution():
    kids_in_swansons_class = 25
    kids_in_jones_class = 32
    zits_per_kid_in_swansons_class = 5
    zits_per_kid_in_jones_class = 6
    total_zits_in_swansons_class = kids_in_swansons_class * zits_per_kid_in_swansons_class
    total_zits_in_jones_class = kids_in_jones_class * zits_per_kid_in_jones_class
    difference = total_zits_in_jones_class - total_zits_in_swansons_class
    result = difference
    return result

print(solution())