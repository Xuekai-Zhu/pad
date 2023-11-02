def solution():
    """A yearly book sale is held in school where students can sell their old books at a cheaper price. Two-fifths of Lovely's books can be sold for $2.50 each and the rest for $2 each. How much will Lovely earn if all 10 books were sold?"""
    # Define the total number of books and the fraction sold for $2.50
    total_books = 10
    fraction_expensive = 2/5

    # Calculate the number of expensive books and the number of cheap books
    num_expensive = int(total_books * fraction_expensive)
    num_cheap = total_books - num_expensive

    # Calculate the total earnings
    earnings = (num_expensive * 2.5) + (num_cheap * 2)

    result = earnings
    return result

print(solution())