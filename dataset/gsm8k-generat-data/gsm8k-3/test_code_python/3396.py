def solution():
    """Remy sold 55 bottles of soda in the morning. Nick sold six fewer bottles of soda than Remy. The price per bottle is $.50. If their total evening sales are $55, how much more did they earn in the evening than in the morning?"""
    # Define the number of soda bottles sold in the morning by Remy
    remy_bottles = 55

    # Define the number of soda bottles sold in the morning by Nick
    nick_bottles = remy_bottles - 6

    # Calculate the total revenue from morning sales
    morning_revenue = (remy_bottles + nick_bottles) * 0.5

    # Calculate the evening sales revenue
    evening_revenue = 55

    # Calculate the difference in revenue
    revenue_difference = evening_revenue - morning_revenue

    # Display the revenue difference
    result = revenue_difference
    return result

print(solution())