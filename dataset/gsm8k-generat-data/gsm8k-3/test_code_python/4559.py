def solution():
    """Marina had 4.5 pounds of fudge. Lazlo had 6 ounces less than 4 pounds of fudge. How many more ounces of fudge did Marina have than Lazlo?"""
    # Convert Marina's amount to ounces
    marina_ounces = 4.5 * 16

    # Calculate Lazlo's amount in ounces
    lazlo_ounces = (4 * 16) - 6

    # Calculate the difference in ounces
    difference_ounces = marina_ounces - lazlo_ounces

    # Display the difference in ounces
    result = difference_ounces
    return result

print(solution())