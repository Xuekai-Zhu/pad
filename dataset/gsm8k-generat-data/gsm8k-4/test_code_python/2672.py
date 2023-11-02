def solution():
    """In a house of 15, 3/5 of the people eat pizza. If Aviana brought pizza with 50 pieces, and each person eating pizza took 4 pieces, calculate the number of pizza pieces that remained."""
    # Define the number of people in the house and the fraction that eats pizza
    total_people = 15
    pizza_eaters_fraction = 3/5

    # Calculate the number of people who eat pizza
    pizza_eaters = total_people * pizza_eaters_fraction

    # Calculate the total number of pizza pieces eaten
    total_pizza_pieces_eaten = pizza_eaters * 4

    # Calculate the number of pizza pieces left
    pizza_pieces_left = 50 - total_pizza_pieces_eaten

    # return the result
    result = pizza_pieces_left
    return result

print(solution())