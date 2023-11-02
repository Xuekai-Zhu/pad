def solution():
    # Calculate Cindy's total earnings from teaching 4 math courses for 48 hours a week
    total_hours = 48   # total hours Cindy works per week
    hourly_rate = 25   # Cindy's hourly rate
    total_earnings = total_hours * 4 * hourly_rate  # total earnings for the month (4 weeks)

    # Calculate the amount Cindy earns for teaching 1 math course in a month
    earnings_per_course = total_earnings / 4   # Cindy teaches 4 math courses
    result = earnings_per_course
    return result

print(solution())