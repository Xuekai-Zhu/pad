def solution():
    """Colleen is making a batch of 48 cookies. She's going to add 108 chocolate chips and one-third as many M&Ms to the whole batch. What are the average number of chocolate pieces in each cookie?"""

    # Calculate the total number of chocolate pieces
    total_chocolate_pieces = 108 + (1/3 * 108)

    # Calculate the average number of chocolate pieces per cookie
    chocolate_per_cookie = total_chocolate_pieces / 48

    # Display the average number of chocolate pieces per cookie
    result = chocolate_per_cookie
    return result

print(solution())