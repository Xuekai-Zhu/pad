def solution():
    josiah_savings = 0.25 * 24  # Josiah saves 0.25 dollars per day for 24 days
    leah_savings = 0.50 * 20  # Leah saves 0.50 dollars per day for 20 days
    megan_savings = 2 * leah_savings  # Megan saves twice as much as Leah for 12 days
    total_savings = josiah_savings + leah_savings + megan_savings  # Total savings of all three children
    result = total_savings
    return result

print(solution())