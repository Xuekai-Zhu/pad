def solution():
    """Josiah puts a quarter in his piggy bank every day for 24 days. Leah saves 50 cents in an empty pickle jar every day for 20 days.
    Megan saves twice as much as Leah for 12 days. How much do the three children save together?"""
    josiah_total = 24 * 0.25
    leah_total = 20 * 0.5
    megan_total = 12 * 1.0
    total_savings = josiah_total + leah_total + megan_total
    result = total_savings
    return result

print(solution())