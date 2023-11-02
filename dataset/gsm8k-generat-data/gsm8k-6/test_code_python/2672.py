def solution():
    # Calculate the total number of people in the house who eat pizza
    pizza_eating_people = (3/5) * 15
    # Calculate the total number of pizza pieces eaten
    total_pizza_pieces_eaten = pizza_eating_people * 4
    # Calculate the number of pizza pieces remaining
    pizza_pieces_remaining = 50 - total_pizza_pieces_eaten
    result = pizza_pieces_remaining
    return result

print(solution())