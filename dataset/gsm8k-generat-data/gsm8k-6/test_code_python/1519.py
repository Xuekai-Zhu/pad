def solution():
    # Calculate the total amount earned by Sandy on Friday, Saturday and Sunday
    friday_earnings = 15 * 10  # Sandy earns $15 per hour and worked 10 hours on Friday
    saturday_earnings = 15 * 6  # Sandy earns $15 per hour and worked 6 hours on Saturday
    sunday_earnings = 15 * 14  # Sandy earns $15 per hour and worked 14 hours on Sunday
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())