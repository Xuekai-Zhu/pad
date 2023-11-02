def solution():
    """Josiah puts a quarter in his piggy bank every day for 24 days. Leah saves 50 cents in an empty pickle jar every day for 20 days. Megan saves twice as much as Leah for 12 days. How much do the three children save together?"""
    josiah_total = 0.25 * 24
    leah_total = 0.50 * 20
    megan_total = 2 * leah_total * 12
    total_savings = josiah_total + leah_total + megan_total
    result = total_savings
    return result

print(solution())