def solution():
    """Marina had 4.5 pounds of fudge. Lazlo had 6 ounces less than 4 pounds of fudge. How many more ounces of fudge did Marina have than Lazlo?"""
    marina_fudge = 4.5 * 16  # convert to ounces
    lazlo_fudge = (4 * 16) - 6  # convert to ounces and subtract 6
    difference = marina_fudge - lazlo_fudge
    result = difference
    return result

print(solution())