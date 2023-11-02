def solution():
    hourly_wage = 10  # Hallie earns $10 per hour
    monday_hours = 7  # Hallie works 7 hours on Monday
    tuesday_hours = 5  # Hallie works 5 hours on Tuesday
    wednesday_hours = 7  # Hallie works 7 hours on Wednesday
    monday_tips = 18  # Hallie receives $18 in tips on Monday
    tuesday_tips = 12  # Hallie receives $12 in tips on Tuesday
    wednesday_tips = 20  # Hallie receives $20 in tips on Wednesday

    # Calculate the total earnings for each day
    monday_earnings = (hourly_wage * monday_hours) + monday_tips
    tuesday_earnings = (hourly_wage * tuesday_hours) + tuesday_tips
    wednesday_earnings = (hourly_wage * wednesday_hours) + wednesday_tips

    # Calculate the total earnings for the three days
    total_earnings = monday_earnings + tuesday_earnings + wednesday_earnings
    result = total_earnings
    return result

print(solution())