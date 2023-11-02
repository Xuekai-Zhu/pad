def solution():
    # Define the number of chicken pieces and the number of friends
    chicken_pieces = 11
    friends = (chicken_pieces - 1) / 2

    # Round up to the nearest integer to account for any remaining chicken pieces
    friends = math.ceil(friends)

    result = friends
    return result

print(solution())