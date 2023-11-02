def solution():
    marina_fudge_pounds = 4.5
    lazlo_fudge_pounds = 4 - 6/16  # 6 ounces less than 4 pounds
    marina_fudge_ounces = marina_fudge_pounds * 16  # convert pounds to ounces
    lazlo_fudge_ounces = lazlo_fudge_pounds * 16
    difference_ounces = marina_fudge_ounces - lazlo_fudge_ounces
    result = difference_ounces
    return result

print(solution())