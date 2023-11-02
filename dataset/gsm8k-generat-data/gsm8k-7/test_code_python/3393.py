def solution():
    tomas_fudge = 1.5
    katya_fudge = 0.5
    boris_fudge = 2

    # Convert pounds to ounces
    tomas_ounces = tomas_fudge * 16
    katya_ounces = katya_fudge * 16
    boris_ounces = boris_fudge * 16

    # Calculate the total amount of fudge in ounces
    total_ounces = tomas_ounces + katya_ounces + boris_ounces
    result = total_ounces
    return result

print(solution())