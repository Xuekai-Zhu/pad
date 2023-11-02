def solution():
    """Krystian works in the library. He borrows an average of 40 books every day. Every Friday, his number of borrowed books is about 40% higher than the daily average. How many books does he borrow in a week if the library is open from Monday to Friday?"""
    # Define the daily average number of borrowed books
    daily_average = 40

    # Calculate the number of borrowed books on Friday
    friday_borrowed = daily_average * 1.4

    # Calculate the total number of borrowed books from Monday to Friday
    total_borrowed = (daily_average * 4) + friday_borrowed

    # Return the result
    result = total_borrowed
    return result

print(solution())