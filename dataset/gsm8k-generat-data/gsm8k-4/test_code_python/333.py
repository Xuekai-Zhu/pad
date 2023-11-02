def solution():
    """Kantana loves chocolate. Every Saturday she goes to the candy store and buys 2 chocolates for herself and 1 for her sister. This last Saturday she picked up an additional 10 chocolates as a birthday gift for her friend Charlie. How many chocolates did Kantana end up buying for the month?"""
    # Define the number of Saturdays in a month
    SATURDAYS = 4

    # Define the number of chocolates Kantana buys for herself and her sister each Saturday
    CHOCOLATES_PER_SATURDAY = 3

    # Define the number of additional chocolates Kantana bought for her friend Charlie
    ADDITIONAL_CHOCOLATES = 10

    # Calculate the total number of chocolates Kantana bought for the month
    total_chocolates = SATURDAYS * CHOCOLATES_PER_SATURDAY + ADDITIONAL_CHOCOLATES

    # return the result
    result = total_chocolates
    return result

print(solution())