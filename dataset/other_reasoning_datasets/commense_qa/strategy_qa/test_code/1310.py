def solution():
    six_year_old_weight = 45
    ten_gallons_seawater_weight = 8 * 10
    if ten_gallons_seawater_weight > six_year_old_weight:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())