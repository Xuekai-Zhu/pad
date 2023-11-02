def solution():
    # Calculate Diana's earnings in August and September
    earnings_august = 150 * 3  # Diana earned 3 times her July earnings in August
    earnings_september = earnings_august * 2  # Diana earned twice as much in September as she did in August

    # Calculate Diana's total earnings over three months
    total_earnings = 150 + earnings_august + earnings_september
    result = total_earnings
    return result

print(solution())