def solution():
    """In a house of 15, 3/5 of the people eat pizza. If Aviana brought pizza with 50 pieces, and each person eating pizza took 4 pieces, calculate the number of pizza pieces that remained."""
    # Calculate the number of people in the house who eat pizza
    people_eating_pizza = 3/5 * 15

    # Calculate the total number of pizza pieces eaten
    pizza_pieces_eaten = people_eating_pizza * 4

    # Calculate the number of pizza pieces remaining
    pizza_pieces_remaining = 50 - pizza_pieces_eaten

    # Display the number of pizza pieces remaining
    result = pizza_pieces_remaining
    return result

print(solution())