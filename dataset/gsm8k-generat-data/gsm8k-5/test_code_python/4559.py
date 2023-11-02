def solution():
    marina_fudge = 4.5 * 16  # Convert 4.5 pounds to ounces
    lazlo_fudge = (4 - 0.375) * 16 - 6  # Convert 4 pounds to ounces, subtract 6 ounces

    # Calculate the difference in ounces between Marina and Lazlo's fudge
    ounces_difference = marina_fudge - lazlo_fudge
    result = ounces_difference
    return result

print(solution())