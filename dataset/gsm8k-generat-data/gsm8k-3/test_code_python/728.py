def solution():
    """Whitney’s mom gave her two $20 bills to spend at the school book fair. Whitney has decided to buy 2 posters, 3 notebooks, and 2 bookmarks. Each poster costs $5, each notebook costs $4, and each bookmark costs $2. How much money, in dollars, will Whitney have left over after the purchase?"""
    # Define the cost of each item
    POSTER_PRICE = 5
    NOTEBOOK_PRICE = 4
    BOOKMARK_PRICE = 2

    # Define the number of each item purchased
    num_posters = 2
    num_notebooks = 3
    num_bookmarks = 2

    # Calculate the total cost of the purchase
    total_cost = (num_posters * POSTER_PRICE) + (num_notebooks * NOTEBOOK_PRICE) + (num_bookmarks * BOOKMARK_PRICE)

    # Calculate the amount of money left over
    money_left = (2 * 20) - total_cost

    # Display the amount of money left over
    result = money_left
    return result

print(solution())