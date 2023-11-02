def solution():
    """From March to August, Sam made $460 doing 23 hours of yard work. However, from September to February, Sam was only able to work for 8 hours. If Sam is saving up to buy a video game console that costs $600 and has already spent $340 to fix his car, how many more hours does he need to work before he can buy the video game console?"""
    # Define the total earnings from yard work
    yard_earnings = 460

    # Define the total number of hours worked for yard work
    yard_hours = 23

    # Define the earnings per hour for yard work
    yard_earnings_per_hour = yard_earnings / yard_hours

    # Define the earnings from the 8 hours of work
    other_earnings = yard_earnings_per_hour * 8

    # Define the total earnings
    total_earnings = yard_earnings + other_earnings

    # Define the total cost of the video game console and the car repair
    total_cost = 600 + 340

    # Calculate the remaining amount needed to buy the video game console
    remaining_amount = total_cost - total_earnings

    # Calculate the number of hours needed to earn the remaining amount
    hours_needed = remaining_amount / yard_earnings_per_hour

    result = round(hours_needed)
    return result

print(solution())