def solution():
    """Mrs. Crocker made 11 pieces of fried chicken for Lyndee and her friends. If Lyndee only ate one piece but each of her friends got to eat 2 pieces, how many friends did Lyndee have over?"""
    total_chicken_pieces = 11
    lyndee_pieces = 1
    friends_pieces = 2
    friends_count = (total_chicken_pieces - lyndee_pieces) / friends_pieces
    result = friends_count
    return result

print(solution())