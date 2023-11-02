def solution():
    """For his birthday, Aku invited 4 friends. His mother bought 3 packages of cookies each containing 25 cookies. After playing football, the children came to eat and celebrate Aku's 10th birthday, each eating an equal number of all the cookies. Calculate the number of cookies that each child will eat."""

    # Define the total number of cookies
    total_cookies = 3 * 25

    # Define the number of children
    num_children = 5

    # Calculate the number of cookies each child will eat
    cookies_per_child = total_cookies // num_children

    # Display the number of cookies each child will eat
    result = cookies_per_child
    return result

print(solution())