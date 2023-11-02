def solution():
    """Whitney’s mom gave her two $20 bills to spend at the school book fair. Whitney has decided to buy 2 posters, 3 notebooks, and 2 bookmarks. Each poster costs $5, each notebook costs $4, and each bookmark costs $2. How much money, in dollars, will Whitney have left over after the purchase?"""
    # Define the prices of posters, notebooks, and bookmarks
    poster_price = 5
    notebook_price = 4
    bookmark_price = 2

    # Calculate the total cost of the purchase
    total_cost = (2 * poster_price) + (3 * notebook_price) + (2 * bookmark_price)

    # Calculate the total amount of money Whitney has
    total_money = 2 * 20

    # Calculate the amount of money Whitney will have left over after the purchase
    money_left = total_money - total_cost

    # Return the result
    result = money_left
    return result

print(solution())