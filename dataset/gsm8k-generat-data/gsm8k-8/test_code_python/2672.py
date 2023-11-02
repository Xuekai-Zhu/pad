def solution():
    # Calculate the number of people in the house who ate pizza
    num_ppl_eating_pizza = 15 * 3/5

    # Calculate the total number of pizza pieces consumed
    total_pizza_pieces_consumed = num_ppl_eating_pizza * 4

    # Calculate the number of pizza pieces that remained
    num_pizza_pieces_remaining = 50 - total_pizza_pieces_consumed
    result = num_pizza_pieces_remaining
    return result

print(solution())