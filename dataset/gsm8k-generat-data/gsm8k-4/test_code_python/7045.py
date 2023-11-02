def solution():
    """Jackson wants to go on a shopping spree, so his mom says she will give him some spending money if he does extra chores. She promises $5 per hour spent on chores. Jackson spends 2 hours vacuuming, and decides to do this twice. He also spends 0.5 hours washing dishes, and three times as long cleaning the bathroom. How much spending money has Jackson earned?"""
    # Define the hourly rate for chores
    hourly_rate = 5

    # Calculate the total hours spent on each chore
    vacuuming_hours = 4
    dishes_hours = 0.5
    bathroom_hours = 3 * dishes_hours

    # Calculate the total earnings from each chore
    vacuuming_earnings = vacuuming_hours * hourly_rate
    dishes_earnings = dishes_hours * hourly_rate
    bathroom_earnings = bathroom_hours * hourly_rate

    # Calculate the total earnings
    total_earnings = vacuuming_earnings + dishes_earnings + bathroom_earnings

    result = total_earnings
    return result

print(solution())