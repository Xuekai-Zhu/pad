def solution():
    """Kantana loves chocolate. Every Saturday she goes to the candy store and buys 2 chocolates for herself and 1 for her sister. This last Saturday she picked up an additional 10 chocolates as a birthday gift for her friend Charlie. How many chocolates did Kantana end up buying for the month?"""
    # Define the number of chocolates Kantana buys each week
    chocolates_per_week = 3

    # Calculate the total number of chocolates Kantana buys in a month
    chocolates_per_month = chocolates_per_week * 4

    # Add the extra chocolates Kantana bought for her friend
    total_chocolates = chocolates_per_month + 10

    # Display the total number of chocolates Kantana bought for the month
    result = total_chocolates
    return result

print(solution())