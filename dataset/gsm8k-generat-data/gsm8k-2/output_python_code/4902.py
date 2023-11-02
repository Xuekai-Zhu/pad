def solution():
    """Margo donated $4300 to Jayden's fundraising campaign. If Julie donated $4700 to Jayden's campaign, What's half the difference in the amount they contributed?"""
    margo_donation = 4300
    julie_donation = 4700
    difference = abs(margo_donation - julie_donation)
    result = difference / 2
    return result

print(solution())