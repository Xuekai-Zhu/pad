def solution():
    """Mikaela earns $10 an hour  tutoring. For the first month, she tutored for 35 hours and in the second month, she tutored 5 hours more than the first month. She spent 4/5 of her total earnings on her personal needs and saved the rest of the money. How much did she save?"""
    # Mikaela's rate per hour
    RATE = 10

    # Mikaela's earnings for the first month
    earnings1 = RATE * 35

    # Mikaela's earnings for the second month
    earnings2 = RATE * (35 + 5)

    # Mikaela's total earnings
    total_earnings = earnings1 + earnings2

    # Calculate how much Mikaela spent on personal needs
    personal_spending = total_earnings * (4/5)

    # Calculate how much Mikaela saved
    savings = total_earnings - personal_spending

    # Display how much Mikaela saved
    result = savings
    return result

print(solution())