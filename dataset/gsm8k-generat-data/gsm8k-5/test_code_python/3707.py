def solution():
    total_cookies = 48  # Colleen is making a batch of 48 cookies
    total_chocolate_chips = 108  # Colleen is adding 108 chocolate chips to the whole batch
    total_MMs = total_chocolate_chips / 3  # Colleen is adding one-third as many M&Ms as chocolate chips to the whole batch

    # Calculate the total number of chocolate pieces in the batch
    total_chocolate_pieces = total_chocolate_chips + total_MMs

    # Calculate the average number of chocolate pieces in each cookie
    average_chocolate_pieces = total_chocolate_pieces / total_cookies
    result = average_chocolate_pieces
    return result

print(solution())