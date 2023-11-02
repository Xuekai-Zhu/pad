def solution():
    """Colleen is making a batch of 48 cookies. She's going to add 108 chocolate chips and one-third as many M&Ms to the whole batch. What are the average number of chocolate pieces in each cookie?"""
    # Define the total number of chocolate chips
    total_chocolate_chips = 108

    # Calculate the total number of M&Ms
    total_mms = total_chocolate_chips / 3

    # Calculate the total number of candy pieces
    total_candies = total_chocolate_chips + total_mms

    # Calculate the average number of candy pieces per cookie
    avg_candies_per_cookie = total_candies / 48

    # Calculate the average number of chocolate chips per cookie
    avg_chocolate_chips_per_cookie = total_chocolate_chips / 48

    # Calculate the average number of chocolate pieces per cookie
    avg_chocolate_pieces_per_cookie = avg_candies_per_cookie - avg_chocolate_chips_per_cookie

    # return the result
    result = avg_chocolate_pieces_per_cookie
    return result

print(solution())