def solution():
    # Define the fraction of books sold for $2.50
    fraction_sold_high = 2/5

    # Define the fraction of books sold for $2.00
    fraction_sold_low = 1 - fraction_sold_high

    # Define the price of books sold for $2.50
    price_high = 2.50

    # Define the price of books sold for $2.00
    price_low = 2.00

    # Define the number of books Lovely has
    total_books = 10

    # Calculate the number of books sold for $2.50
    num_sold_high = fraction_sold_high * total_books

    # Calculate the amount earned from books sold for $2.50
    earned_high = num_sold_high * price_high

    # Calculate the number of books sold for $2.00
    num_sold_low = fraction_sold_low * total_books

    # Calculate the amount earned from books sold for $2.00
    earned_low = num_sold_low * price_low

    # Calculate the total amount earned
    total_earned = earned_high + earned_low
    result = total_earned
    return result

print(solution())