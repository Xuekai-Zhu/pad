def solution():
    """Mrs. Crocker made 11 pieces of fried chicken for Lyndee and her friends. If Lyndee only ate one piece but each of her friends got to eat 2 pieces, how many friends did Lyndee have over?"""
    # Define the total number of chicken pieces and the number that Lyndee ate
    total_chicken_pieces = 11
    lyndee_chicken_pieces = 1

    # Calculate the number of chicken pieces that Lyndee's friends ate
    friends_chicken_pieces = total_chicken_pieces - lyndee_chicken_pieces

    # Calculate the number of friends that Lyndee had over
    num_friends = friends_chicken_pieces // 2

    # return the result
    result = num_friends
    return result

print(solution())