def solution():
    pounds = 42
    euros = 11
    yen = 3000

    # Convert pounds to yen
    pounds_to_yen = pounds * 100

    # Convert euros to yen
    euros_to_yen = euros * 2 * 100

    # Add all yen amounts
    total_yen = yen + pounds_to_yen + euros_to_yen

    result = total_yen
    return result

print(solution())