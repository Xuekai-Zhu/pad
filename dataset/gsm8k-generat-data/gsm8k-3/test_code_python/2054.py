def solution():
    """A new book sold 15 copies at the bookstore on Wednesday. On Thursday the book sold three times that many copies. On Friday the book sold one-fifth the number of copies it did on Thursday. How many copies of the book did the bookstore sell by Friday?"""
    # Define the number of copies sold on Wednesday
    copies_wednesday = 15

    # Calculate the number of copies sold on Thursday
    copies_thursday = copies_wednesday * 3

    # Calculate the number of copies sold on Friday
    copies_friday = copies_thursday / 5

    # Calculate the total number of copies sold
    total_copies = copies_wednesday + copies_thursday + copies_friday

    # Display the total number of copies sold
    result = total_copies
    return result

print(solution())