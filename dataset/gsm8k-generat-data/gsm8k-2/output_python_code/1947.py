def solution():
    """Tonya has opened a lemonade stand selling lemonade in small, medium, and large cups at $1, $2 and $3 respectively. At the close of business she ended up making $50. As she went back through her inventory she noticed that she sold $11 worth of small lemonades and $24 worth of medium lemonades. How many cups of large lemonade did Tonya sell?"""
    small_price = 1
    medium_price = 2
    large_price = 3
    total_sales = 50
    small_sales = 11
    medium_sales = 24
    # Let's assume Tonya sold x cups of large lemonade
    # Then we can write an equation for total sales
    # small_sales + medium_sales + large_sales = total_sales
    # small_cups_sold * small_price + medium_cups_sold * medium_price + large_cups_sold * large_price = total_sales
    # We know small_sales and medium_sales, we need to solve for large_sales
    # We also know that the total number of cups sold is the sum of cups sold for all sizes
    # small_cups_sold + medium_cups_sold + large_cups_sold = total_cups_sold
    # We can solve for large_cups_sold using the above two equations
    total_cups_sold = small_sales / small_price + medium_sales / medium_price + large_sales / large_price
    large_sales = (total_sales - small_sales - medium_sales) * (large_price / (small_price + medium_price + large_price))
    result = large_sales
    return result

print(solution())