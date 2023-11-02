def solution():
    """Marina had 4.5 pounds of fudge. Lazlo had 6 ounces less than 4 pounds of fudge. How many more ounces of fudge did Marina have than Lazlo?"""
    # Convert Marina's fudge to ounces
    marina_fudge = 4.5 * 16

    # Convert Lazlo's fudge to ounces (4 pounds = 64 ounces)
    lazlo_fudge = (4 * 16) - 6

    # Calculate the difference in ounces between Marina's and Lazlo's fudge
    diff = marina_fudge - lazlo_fudge

    # Return the result
    result = diff
    return result

print(solution())