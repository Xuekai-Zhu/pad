def solution():
    cookies_sold = 50  # Joe sold 50 cookies
    total_earnings = 60  # Joe earned $60
    markup_percentage = 20  # Joe sells the cookies for 20% more than it costs to make them

    # Calculate the price Joe sells each cookie for
    price_per_cookie = total_earnings / cookies_sold

    # Calculate the cost per cookie before markup
    cost_per_cookie = price_per_cookie / (1 + (markup_percentage / 100))

    result = cost_per_cookie
    return result

print(solution())