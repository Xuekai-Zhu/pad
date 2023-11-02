def solution():
    """John makes 6 dozen cookies for a bake sale.  He sells each cookie for $1.5 and each cookie costs $0.25 to make.  He splits the profit between two charities evenly.  How much does each charity get?"""
    # Define the cost to make each cookie
    COST_PER_COOKIE = 0.25

    # Define the number of cookies made
    cookies_made = 6 * 12

    # Calculate the total revenue from selling the cookies
    total_revenue = cookies_made * 1.5

    # Calculate the total cost to make the cookies
    total_cost = cookies_made * COST_PER_COOKIE

    # Calculate the total profit
    total_profit = total_revenue - total_cost

    # Calculate the amount each charity will receive
    charity_amount = total_profit / 2

    # Display the amount each charity will receive
    result = charity_amount
    return result

print(solution())