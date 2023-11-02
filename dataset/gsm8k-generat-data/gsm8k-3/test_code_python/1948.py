def solution():
    """Tonya has opened a lemonade stand selling lemonade in small, medium, and large cups at $1, $2 and $3 respectively. At the close of business she ended up making $50.
    As she went back through her inventory she noticed that she sold $11 worth of small lemonades and $24 worth of medium lemonades. How many cups of large lemonade did Tonya sell?"""
    # Define the price of each size of lemonade
    SMALL_PRICE = 1
    MEDIUM_PRICE = 2
    LARGE_PRICE = 3

    # Define the total earnings and amount of small and medium cups sold
    total_earnings = 50
    small_cups_sold = 11
    medium_cups_sold = 24

    # Calculate the total earnings from large cups
    large_earnings = total_earnings - small_cups_sold - medium_cups_sold

    # Calculate the number of large cups sold
    large_cups_sold = large_earnings // LARGE_PRICE

    # Display the number of large cups sold
    result = large_cups_sold
    return result

print(solution())