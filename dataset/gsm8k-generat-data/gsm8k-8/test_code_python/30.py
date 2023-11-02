def solution():
    # Define the total number of pieces in a single pizza
    pieces_per_pizza = 4

    # Calculate the total number of pizzas bought
    total_pizzas = 4

    # Calculate the number of pizza pieces eaten by each person
    bill_dale_pieces = 0.5 * pieces_per_pizza * 2
    ann_cate_pieces = 0.75 * pieces_per_pizza * 2

    # Calculate the total number of pizza pieces eaten
    total_pieces_eaten = bill_dale_pieces + ann_cate_pieces

    # Calculate the total number of pizza pieces left uneaten
    total_pieces_left = total_pizzas * pieces_per_pizza - total_pieces_eaten
    result = total_pieces_left

    return result

print(solution())