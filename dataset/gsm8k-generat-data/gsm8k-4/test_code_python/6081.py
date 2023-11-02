def solution():
    """Joe sells cookies for 20% more than it costs to make them. If he sold 50 cookies and earned $60, how much do the cookies cost to make?"""
    # Define the variables
    cookies_sold = 50
    profit = 60
    markup_percentage = 0.2

    # Calculate the revenue from selling cookies
    revenue = cookies_sold * (profit / cookies_sold)

    # Calculate the cost of making the cookies
    cost = revenue / (1 + markup_percentage)

    # Return the cost
    result = cost
    return result

print(solution())