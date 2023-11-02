def solution():
    gallons_roman = 3 * (gallons_remy - 1)
    total_gallons = 33
    gallons_remy = total_gallons - gallons_roman
    result = gallons_remy
    return result

print(solution())