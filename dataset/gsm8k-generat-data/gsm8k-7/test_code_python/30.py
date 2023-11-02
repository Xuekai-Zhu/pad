def solution():
    num_people = 4
    num_pieces_per_pizza = 4

    # Calculate the total number of pizza pieces
    total_pieces = num_people * num_pieces_per_pizza

    # Calculate the number of pizza pieces eaten by Bill and Dale
    bill_dale_pieces = 0.5 * 2 * num_pieces_per_pizza

    # Calculate the number of pizza pieces eaten by Ann and Cate
    ann_cate_pieces = 0.75 * 2 * num_pieces_per_pizza

    # Calculate the total number of pizza pieces left uneaten
    uneaten_pieces = total_pieces - bill_dale_pieces - ann_cate_pieces
    result = uneaten_pieces
    return result

print(solution())