def solution():
    # Calculate the total amount Josiah saves in 24 days
    josiah_savings = 0.25 * 24

    # Calculate the total amount Leah saves in 20 days
    leah_savings = 0.50 * 20

    # Calculate the total amount Megan saves in 12 days
    megan_savings = 2 * leah_savings * 12

    # Calculate the total savings of all three children together
    total_savings = josiah_savings + leah_savings + megan_savings
    result = total_savings
    return result

print(solution())