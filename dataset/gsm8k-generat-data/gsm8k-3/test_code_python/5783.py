def solution():
    """Josiah puts a quarter in his piggy bank every day for 24 days.  Leah saves 50 cents in an empty pickle jar every day for 20 days. Megan saves twice as much as Leah for 12 days.   How much do the three children save together?"""
    # Calculate Josiah's savings
    josiah_savings = 0.25 * 24

    # Calculate Leah's savings
    leah_savings = 0.5 * 20

    # Calculate Megan's savings
    megan_savings = 2 * leah_savings * 12

    # Calculate the total savings
    total_savings = josiah_savings + leah_savings + megan_savings

    # Display the total savings
    result = total_savings
    return result

print(solution())