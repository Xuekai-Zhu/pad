def solution():
    # Calculate the total cost and revenue of making and selling the cookies
    total_cookies = 6*12  # John makes 6 dozen cookies, which is 6*12 = 72 cookies
    cost_of_cookies = 0.25*total_cookies  # each cookie costs $0.25 to make
    revenue_from_cookies = 1.5*total_cookies  # John sells each cookie for $1.5
    profit = revenue_from_cookies - cost_of_cookies  # John's profit from selling the cookies
    each_charity = profit / 2  # John splits the profit between two charities evenly

    result = each_charity
    return result

print(solution())