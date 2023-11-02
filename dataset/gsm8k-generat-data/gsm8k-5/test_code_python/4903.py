def solution():
    margo_donation = 4300
    julie_donation = 4700

    # Calculate the difference in the amount they contributed
    donation_difference = abs(julie_donation - margo_donation)

    # Calculate half of the difference in the amount they contributed
    half_donation_difference = donation_difference / 2
    result = half_donation_difference
    return result

print(solution())