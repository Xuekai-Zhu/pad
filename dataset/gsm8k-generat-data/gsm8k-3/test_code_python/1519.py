def solution():
    """Sandy earns $15 per hour. She worked 10 hours on Friday with her best friend, 6 hours on Saturday alone and 14 hours on Sunday with her other co-workers. How much money did Sandy earn in all on Friday, Saturday and Sunday?"""
    # Define Sandy's hourly rate
    hourly_rate = 15

    # Define the number of hours Sandy worked on each day
    friday_hours = 10
    saturday_hours = 6
    sunday_hours = 14

    # Calculate Sandy's earnings for each day
    friday_earnings = friday_hours * hourly_rate
    saturday_earnings = saturday_hours * hourly_rate
    sunday_earnings = sunday_hours * hourly_rate

    # Calculate Sandy's total earnings
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings

    # Display Sandy's total earnings
    result = total_earnings
    return result

print(solution())