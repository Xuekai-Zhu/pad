def solution():
    """On Thursday Walmart sold 210 pounds of ground beef. On Friday they sold twice that amount. On Saturday they only sold 150 pounds. What was the average amount of beef sold per day?"""
    # Define the amount of beef sold on each day
    thursday_amount = 210
    friday_amount = thursday_amount * 2
    saturday_amount = 150

    # Calculate the total amount of beef sold over the three days
    total_amount = thursday_amount + friday_amount + saturday_amount

    # Calculate the average amount of beef sold per day
    average_amount = total_amount / 3

    result = average_amount
    return result

print(solution())