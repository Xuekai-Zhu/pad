def solution():
    total_kids = 40
    kids_in_less_than_6 = total_kids * 0.1
    kids_in_less_than_8 = total_kids * 0.3
    kids_in_more_than_14 = total_kids - kids_in_less_than_6 - kids_in_less_than_8
    result = kids_in_more_than_14
    return result

print(solution())