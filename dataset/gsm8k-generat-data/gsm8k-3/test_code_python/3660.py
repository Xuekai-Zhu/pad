def solution():
    """Marco owns an ice cream truck.  His ice cream cones are $5 each.  If his expenses are 80% of total sales for the day, how many ice cream cones would he need to sell to make a $200 profit for the day?"""
    # Define the price of an ice cream cone and the profit goal
    CONE_PRICE = 5
    PROFIT_GOAL = 200

    # Calculate the total revenue needed to earn the profit goal
    total_revenue = PROFIT_GOAL / 0.2

    # Calculate the number of ice cream cones needed to reach the total revenue
    cones_needed = total_revenue / CONE_PRICE

    # Display the number of ice cream cones needed
    result = cones_needed
    return result

print(solution())