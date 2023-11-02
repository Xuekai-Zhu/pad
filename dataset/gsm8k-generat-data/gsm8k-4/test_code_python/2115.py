def solution():
    """For his birthday, Aku invited 4 friends. His mother bought 3 packages of cookies each containing 25 cookies. After playing football, the children came to eat and celebrate Aku's 10th birthday, each eating an equal number of all the cookies. Calculate the number of cookies that each child will eat."""
    # Define the number of friends and number of cookie packages
    num_friends = 4
    num_packages = 3
    cookies_per_package = 25

    # Calculate the total number of cookies
    total_cookies = num_packages * cookies_per_package

    # Calculate the number of cookies each child will eat
    cookies_per_child = total_cookies / (num_friends + 1)

    # Return the result
    result = cookies_per_child
    return result

print(solution())