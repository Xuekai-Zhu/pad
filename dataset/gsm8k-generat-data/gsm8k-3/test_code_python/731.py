def solution():
    """A clothing store sells 20 shirts and 10 pairs of jeans. A shirt costs $10 each and a pair of jeans costs twice as much. How much will the clothing store earn if all shirts and jeans are sold?"""
    # Define the cost of a shirt and a pair of jeans
    SHIRT_PRICE = 10
    JEANS_PRICE = 2 * SHIRT_PRICE

    # Define the number of shirts and pairs of jeans sold
    shirts_sold = 20
    jeans_sold = 10

    # Calculate the total revenue from selling all shirts
    total_shirt_revenue = SHIRT_PRICE * shirts_sold

    # Calculate the total revenue from selling all pairs of jeans
    total_jeans_revenue = JEANS_PRICE * jeans_sold

    # Calculate the total revenue from selling all the clothes
    total_revenue = total_shirt_revenue + total_jeans_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())