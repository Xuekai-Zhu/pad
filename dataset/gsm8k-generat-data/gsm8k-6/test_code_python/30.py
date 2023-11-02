def solution():
    # Calculate the total number of pizza pieces
    total_pieces = 4 * 4  # 4 personal pan pizzas, each cut into 4 pieces

    # Calculate the number of pieces eaten by Bill and Dale
    bd_pieces = 2 * 4 * 0.5  # Bill and Dale eat 50% of their pizzas

    # Calculate the number of pieces eaten by Ann and Cate
    ac_pieces = 2 * 4 * 0.75  # Ann and Cate eat 75% of the pizzas

    # Calculate the total number of pieces left uneaten
    uneaten_pieces = total_pieces - bd_pieces - ac_pieces
    result = uneaten_pieces
    return result

print(solution())