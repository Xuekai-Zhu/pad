def solution():
    """A yearly book sale is held in school where students can sell their old books at a cheaper price. Two-fifths of Lovely's books can be sold for $2.50 each and the rest for $2 each. How much will Lovely earn if all 10 books were sold?"""
    # Define the prices of the different types of books
    PRICE1 = 2.5
    PRICE2 = 2

    # Define the fraction of Lovely's books that can be sold for PRICE1
    FRACTION1 = 2/5

    # Define the number of books Lovely has
    NUM_BOOKS = 10

    # Calculate the number of books that can be sold for PRICE1 and PRICE2
    num_books1 = int(NUM_BOOKS * FRACTION1)
    num_books2 = NUM_BOOKS - num_books1

    # Calculate Lovely's earnings
    earnings = (num_books1 * PRICE1) + (num_books2 * PRICE2)

    # Display Lovely's earnings
    result = earnings
    return result

print(solution())