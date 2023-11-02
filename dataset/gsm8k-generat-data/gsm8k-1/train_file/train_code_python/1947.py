def solution():
    """Tonya has opened a lemonade stand selling lemonade in small, medium, and large cups at $1, $2 and $3 respectively.
    At the close of business she ended up making $50. As she went back through her inventory she noticed that
    she sold $11 worth of small lemonades and $24 worth of medium lemonades. How many cups of large lemonade did Tonya sell?"""
    total_sales = 50
    small_sales = 11
    medium_sales = 24
    small_price = 1
    medium_price = 2
    large_price = 3
    
    # Use algebra to solve for the unknown, x = number of large cups sold
    # small_cups_sold + medium_cups_sold + large_cups_sold = total_cups_sold
    # small_price*small_cups_sold + medium_price*medium_cups_sold + large_price*large_cups_sold = total_sales
    # small_cups_sold = 11 and medium_cups_sold = 24
    large_cups_sold = (total_sales - (small_sales + medium_sales)) / large_price
    
    result = large_cups_sold
    
    return result

print(solution())