def solution():
    """Josh is saving up for a box of cookies. To raise the money, he is going to make bracelets and sell them. It costs $1 for supplies for each bracelet and he sells each one for $1.5. If he makes 12 bracelets and after buying the cookies still has $3, how much did the box of cookies cost?"""
    # Define the cost and revenue per bracelet
    COST_PER_BRACELET = 1
    REVENUE_PER_BRACELET = 1.5

    # Define the number of bracelets Josh made
    num_bracelets = 12

    # Calculate Josh's total cost to make the bracelets
    total_cost = COST_PER_BRACELET * num_bracelets

    # Calculate Josh's total revenue from selling the bracelets
    total_revenue = REVENUE_PER_BRACELET * num_bracelets

    # Calculate Josh's profit from selling the bracelets
    profit = total_revenue - total_cost

    # Calculate the cost of the box of cookies
    box_cost = profit - 3

    # Display the cost of the box of cookies
    result = box_cost
    return result

print(solution())