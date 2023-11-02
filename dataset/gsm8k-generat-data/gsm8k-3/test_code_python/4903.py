def solution():
    """Margo donated $4300 to Jayden's fundraising campaign. If Julie donated $4700 to Jayden's campaign, What's half the difference in the amount they contributed?"""
    # Define the amount donated by Margo and Julie
    margo_contribution = 4300
    julie_contribution = 4700

    # Calculate the difference in the amount donated
    contribution_diff = abs(margo_contribution - julie_contribution)

    # Calculate half of the difference
    half_diff = contribution_diff / 2

    # Display half the difference
    result = half_diff
    return result

print(solution())