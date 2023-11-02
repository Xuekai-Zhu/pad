def solution():
    """Paul and his sister Paula went to the cookie store to buy some cookies. Paula bought 3 fewer cookies than Paul, who bought 45 cookies. How many cookies do they have altogether?"""
    # Paul bought 45 cookies
    paul_cookies = 45

    # Paula bought 3 fewer cookies than Paul
    paula_cookies = paul_cookies - 3

    # Calculate the total number of cookies
    total_cookies = paul_cookies + paula_cookies

    # Display the total number of cookies
    result = total_cookies
    return result

print(solution())