def solution():
    """From March to August, Sam made $460 doing 23 hours of yard work. However, from September to February, Sam was only able to work for 8 hours. If Sam is saving up to buy a video game console that costs $600 and has already spent $340 to fix his car, how many more hours does he need to work before he can buy the video game console?"""
    # Define Sam's total earnings and hours worked
    total_earnings = 460
    total_hours = 23

    # Calculate Sam's hourly rate in the first 6 months
    hourly_rate = total_earnings / total_hours

    # Calculate Sam's earnings and hours worked in the last 6 months
    earnings_last_six_months = 8 * hourly_rate
    hours_last_six_months = 8

    # Calculate Sam's total earnings and hours worked
    total_earnings += earnings_last_six_months
    total_hours += hours_last_six_months

    # Calculate Sam's total expenses
    total_expenses = 340

    # Calculate Sam's total savings
    total_savings = total_earnings - total_expenses

    # Calculate the remaining amount needed to buy the video game console
    remaining_amount = 600 - total_savings

    # Calculate the number of hours Sam needs to work to earn the remaining amount
    hours_needed = remaining_amount / hourly_rate

    # Display the number of hours Sam needs to work
    result = hours_needed
    return result

print(solution())