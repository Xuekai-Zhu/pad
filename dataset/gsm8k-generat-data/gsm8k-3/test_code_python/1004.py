def solution():
    """Kamil wants to renovate his kitchen at home. For this purpose, he hired two professionals who work for him 6 hours a day for 7 days. What does it cost Kamil to hire these professionals if one of them is paid $15 per hour of work?"""
    # Define the number of workers and hours per day
    num_workers = 2
    hours_per_day = 6

    # Define the rate of pay for one worker per hour
    pay_rate = 15

    # Calculate the total number of hours worked
    total_hours = num_workers * hours_per_day * 7

    # Calculate the total cost of hiring the professionals
    total_cost = total_hours * pay_rate

    # Display the total cost
    result = total_cost
    return result

print(solution())