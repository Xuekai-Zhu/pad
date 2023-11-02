def solution():
    """A new book sold 15 copies at the bookstore on Wednesday. On Thursday the book sold three times that many copies. On Friday the book sold one-fifth the number of copies it did on Thursday. How many copies of the book did the bookstore sell by Friday?"""
    # Define the initial number of copies sold on Wednesday
    copies_sold_wed = 15

    # Calculate the number of copies sold on Thursday
    copies_sold_thu = copies_sold_wed * 3

    # Calculate the number of copies sold on Friday
    copies_sold_fri = copies_sold_thu * 1/5

    # Calculate the total number of copies sold by Friday
    total_copies_sold = copies_sold_wed + copies_sold_thu + copies_sold_fri

    result = total_copies_sold
    return result

print(solution())