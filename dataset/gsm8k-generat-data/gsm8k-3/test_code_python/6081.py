def solution():
    """Joe sells cookies for 20% more than it costs to make them. If he sold 50 cookies and earned $60, how much do the cookies cost to make?"""
    # Define the number of cookies sold and the amount earned
    cookies_sold = 50
    earnings = 60

    # Calculate the average price per cookie
    price_per_cookie = earnings / cookies_sold

    # Calculate the cost per cookie
    cost_per_cookie = price_per_cookie / 1.2

    # Display the cost per cookie
    result = cost_per_cookie
    return result

print(solution())