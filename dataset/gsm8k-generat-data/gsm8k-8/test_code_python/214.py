def solution():
    total_months_in_4_years = 4 * 12
    months_passed_in_6_months = 6

    # Subtract the months passed in 6 months and the remaining months from their 4th anniversary to get the months passed since their 2nd anniversary
    months_passed_since_2nd_anniversary = total_months_in_4_years - months_passed_in_6_months - 24
    result = months_passed_since_2nd_anniversary
    return result

print(solution())