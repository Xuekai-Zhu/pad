def solution():
    # Calculate the total amount saved by Josiah
    josiah_savings = 0.25 * 24  # Josiah puts a quarter in his piggy bank every day for 24 days

    # Calculate the total amount saved by Leah
    leah_savings = 0.50 * 20  # Leah saves 50 cents in an empty pickle jar every day for 20 days

    # Calculate the total amount saved by Megan
    megan_savings = 2 * leah_savings  # Megan saves twice as much as Leah for 12 days

    # Calculate the total amount saved by all three children
    total_savings = josiah_savings + leah_savings + megan_savings

    result = total_savings
    return result

print(solution())