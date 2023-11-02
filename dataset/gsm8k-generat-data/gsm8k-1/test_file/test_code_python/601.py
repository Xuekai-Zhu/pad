def solution():
    """For four hours, Patrick sold 15 cups of lemonade per hour at a price of $0.50 per cup. In the next two hours, he sold 10 cups of lemonade per hour at a price of $0.60 per cup. How much money did Patrick earn, in dollars, from selling lemonade for 6 hours?"""
    cups_sold_4_hours = 15 * 4
    cups_sold_2_hours = 10 * 2
    total_cups_sold = cups_sold_4_hours + cups_sold_2_hours
    total_earned_4_hours = cups_sold_4_hours * 0.50
    total_earned_2_hours = cups_sold_2_hours * 0.60
    total_earned = total_earned_4_hours + total_earned_2_hours
    result = total_earned
    return result

print(solution())