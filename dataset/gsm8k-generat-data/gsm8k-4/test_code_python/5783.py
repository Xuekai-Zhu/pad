def solution():
    """Josiah puts a quarter in his piggy bank every day for 24 days. Leah saves 50 cents in an empty pickle jar every day for 20 days. Megan saves twice as much as Leah for 12 days. How much do the three children save together?"""
    # Calculate the total savings of Josiah
    josiah_savings = 0.25 * 24

    # Calculate the total savings of Leah
    leah_savings = 0.5 * 20

    # Calculate the total savings of Megan
    megan_savings = 2 * leah_savings * 12

    # Calculate the total savings of the three children
    total_savings = josiah_savings + leah_savings + megan_savings

    result = total_savings
    return result

print(solution())