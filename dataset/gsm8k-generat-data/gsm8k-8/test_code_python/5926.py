def solution():
    # Convert euros to pounds
    euro_to_pound = 2
    pounds_from_euros = 11 * euro_to_pound

    # Convert pounds to yen
    pound_to_yen = 100
    pounds_to_yen = (42 + pounds_from_euros) * pound_to_yen

    # Add yen to total
    total_yen = pounds_to_yen + 3000
    result = total_yen
    return result

print(solution())