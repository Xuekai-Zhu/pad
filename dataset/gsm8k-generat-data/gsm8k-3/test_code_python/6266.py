def solution():
    """On Friday, Addison sold 181 raffle tickets for a fundraiser. She sold twice as many on Saturday. On Sunday, she sold 78 raffle tickets. How many more raffle tickets were sold on Saturday than Sunday?"""
    # Define the number of raffle tickets sold on Friday and Sunday
    friday_sales = 181
    sunday_sales = 78

    # Calculate the number of raffle tickets sold on Saturday
    saturday_sales = 2 * friday_sales

    # Calculate the difference in sales between Saturday and Sunday
    difference = saturday_sales - sunday_sales

    # Display the difference in sales
    result = difference
    return result

print(solution())