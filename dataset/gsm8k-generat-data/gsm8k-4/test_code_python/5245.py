def solution():
    """John makes 6 dozen cookies for a bake sale. He sells each cookie for $1.5 and each cookie costs $0.25 to make. He splits the profit between two charities evenly. How much does each charity get?"""
    # Calculate the total number of cookies made
    cookies_made = 6 * 12

    # Calculate the total cost of making the cookies
    total_cost = cookies_made * 0.25

    # Calculate the total revenue from selling the cookies
    total_revenue = cookies_made * 1.5

    # Calculate the total profit
    total_profit = total_revenue - total_cost

    # Calculate the profit for each charity
    charity_profit = total_profit / 2

    # return the result
    result = charity_profit
    return result

print(solution())