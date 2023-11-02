def solution():
    """Laran has started a poster business. She is selling 5 posters per day at school. Two posters per day are her large posters that sell for $10. The large posters cost her $5 to make. The remaining posters are small posters that sell for $6. They cost $3 to produce. How much profit, in dollars, does Laran make per 5-day school week?"""
    # Define the number of days in the school week
    SCHOOL_WEEK_DAYS = 5

    # Define the number of large posters sold per day
    LARGE_POSTERS_SOLD = 2

    # Define the number of small posters sold per day
    SMALL_POSTERS_SOLD = 3

    # Define the cost and selling price of a large poster
    LARGE_POSTER_COST = 5
    LARGE_POSTER_SELLING_PRICE = 10

    # Define the cost and selling price of a small poster
    SMALL_POSTER_COST = 3
    SMALL_POSTER_SELLING_PRICE = 6

    # Calculate the total revenue and cost for the week
    total_large_posters_sold = LARGE_POSTERS_SOLD * SCHOOL_WEEK_DAYS
    total_small_posters_sold = SMALL_POSTERS_SOLD * SCHOOL_WEEK_DAYS
    total_revenue = (total_large_posters_sold * LARGE_POSTER_SELLING_PRICE) + (total_small_posters_sold * SMALL_POSTER_SELLING_PRICE)
    total_cost = (total_large_posters_sold * LARGE_POSTER_COST) + (total_small_posters_sold * SMALL_POSTER_COST)

    # Calculate the profit for the week
    profit = total_revenue - total_cost

    # Display the profit for the week
    result = profit
    return result

print(solution())