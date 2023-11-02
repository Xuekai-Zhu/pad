def solution():
    margo_donation = 4300
    julie_donation = 4700

    # Calculate the difference in the amount donated by Margo and Julie
    difference = abs(margo_donation - julie_donation)

    # Calculate half of the difference
    half_difference = difference / 2
    result = half_difference
    return result

print(solution())