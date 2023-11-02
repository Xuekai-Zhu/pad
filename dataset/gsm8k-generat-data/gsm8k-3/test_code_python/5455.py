def solution():
    """Hank gave his wife, Delphine, a box of 24 chocolates for Valentine's Day.  On the first day, Delphine ate 4 chocolates.  On the second day, she ate 3 less than twice as many chocolates as she ate the first day.  On the third day, she ate two less than the number she ate on the first day.  And on the fourth day, she ate one less than she ate the previous day.  On the fifth day, how many chocolates remained uneaten?"""
    # Define the number of chocolates Delphine ate each day
    chocolates_day1 = 4
    chocolates_day2 = 2 * chocolates_day1 - 3
    chocolates_day3 = chocolates_day1 - 2
    chocolates_day4 = chocolates_day3 - 1

    # Calculate the total number of chocolates Delphine ate
    total_chocolates_eaten = chocolates_day1 + chocolates_day2 + chocolates_day3 + chocolates_day4

    # Calculate the number of chocolates remaining
    chocolates_remaining = 24 - total_chocolates_eaten

    # Display the number of chocolates remaining
    result = chocolates_remaining
    return result

print(solution())