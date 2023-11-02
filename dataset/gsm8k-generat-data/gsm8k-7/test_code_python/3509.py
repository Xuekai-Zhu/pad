def solution():
    # Scott runs 3 miles on Monday, Tuesday, and Wednesday
    weekly_miles = 3 * 3  # 9 miles per week

    # On Thursday and Friday, Scott runs twice as far as he did on Monday (6 miles)
    weekly_miles += 2 * 6  # 12 miles per week

    # Multiply weekly total by 4 weeks in a month
    monthly_miles = weekly_miles * 4
    result = monthly_miles
    return result

print(solution())