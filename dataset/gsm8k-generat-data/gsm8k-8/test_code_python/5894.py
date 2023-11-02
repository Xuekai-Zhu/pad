def solution():
    # Calculate the total hours worked in the week
    total_hours = 6 * 3 + 2 * (40 - 18)  # 18 hours already worked in first 3 days

    # Calculate the total earnings for the first 40 hours
    earnings_for_40_hours = 30 * 40

    if total_hours > 40:
        # Calculate the additional earnings for the hours above 40
        extra_hours = total_hours - 40
        extra_earnings = 1.5 * 30 * extra_hours

        # Calculate the total earnings
        total_earnings = earnings_for_40_hours + extra_earnings
    else:
        total_earnings = earnings_for_40_hours

    result = total_earnings
    return result

print(solution())