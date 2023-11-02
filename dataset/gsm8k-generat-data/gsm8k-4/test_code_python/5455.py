def solution():
    """Hank gave his wife, Delphine, a box of 24 chocolates for Valentine's Day. On the first day, Delphine ate 4 chocolates. On the second day, she ate 3 less than twice as many chocolates as she ate the first day. On the third day, she ate two less than the number she ate on the first day. And on the fourth day, she ate one less than she ate the previous day. On the fifth day, how many chocolates remained uneaten?"""
    # Define the initial number of chocolates
    chocolates = 24

    # Calculate the number of chocolates eaten on the first day and subtract it from the initial number
    chocolates -= 4

    # Calculate the number of chocolates eaten on the second day and subtract it from the remaining number
    chocolates -= (2 * 4) - 3

    # Calculate the number of chocolates eaten on the third day and subtract it from the remaining number
    chocolates -= 4 - 2

    # Calculate the number of chocolates eaten on the fourth day and subtract it from the remaining number
    chocolates -= 3 - 1

    # The number of chocolates remaining uneaten on the fifth day
    result = chocolates
    return result

print(solution())