def solution():
    """Josh is saving up for a box of cookies. To raise the money, he is going to make bracelets and sell them. It costs $1 for supplies for each bracelet and he sells each one for $1.5. If he makes 12 bracelets and after buying the cookies still has $3, how much did the box of cookies cost?"""
    # Define the cost and selling price of each bracelet
    BRACELET_COST = 1
    BRACELET_PRICE = 1.5

    # Calculate the total profit from selling bracelets
    total_profit = (BRACELET_PRICE - BRACELET_COST) * 12

    # Calculate the cost of the box of cookies
    cookie_cost = total_profit - 3

    # Return the result
    result = cookie_cost
    return result

print(solution())