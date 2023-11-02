def solution():
    small_price = 1  # Small lemonade costs $1
    medium_price = 2  # Medium lemonade costs $2
    large_price = 3  # Large lemonade costs $3
    total_sales = 50  # Tonya made $50 in total

    # Calculate the number of small and medium cups sold
    small_cups_sold = 11 / small_price 
    medium_cups_sold = 24 / medium_price 

    # Calculate the total sales of large cups and the number of large cups sold
    large_sales = total_sales - 11 - 24
    large_cups_sold = large_sales / large_price 
    result = large_cups_sold
    return result

print(solution())