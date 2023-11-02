def solution():
    # Calculate MegaCorp's daily earnings
    daily_earnings = (3000000 + 5000000) - 30000000 / 30

    # Calculate MegaCorp's annual earnings
    annual_earnings = daily_earnings * 365

    # Calculate MegaCorp's fine
    fine = annual_earnings * 0.01

    result = fine
    return result

print(solution())