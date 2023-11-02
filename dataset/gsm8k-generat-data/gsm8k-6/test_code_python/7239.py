def solution():
    # Calculate Scout's earnings on Saturday
    saturday_earnings = 10*4 + 5*5  # worked 4 hours and delivered groceries to 5 people

    # Calculate Scout's earnings on Sunday
    sunday_earnings = 10*5 + 5*8  # worked 5 hours and delivered groceries to 8 people

    # Calculate Scout's total earnings over the weekend
    total_earnings = saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())