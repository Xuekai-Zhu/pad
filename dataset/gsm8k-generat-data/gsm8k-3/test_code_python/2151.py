def solution():
    """Charley bought 30 pencils. She lost 6 pencils while moving to school, and of course, also lost 1/3 of the remaining pencils because she wasn't very good at keeping track of pencils. How many pencils does she currently have?"""
    # Define the initial number of pencils
    initial_pencils = 30

    # Calculate the number of lost pencils during the move
    lost_pencils_move = 6

    # Calculate the remaining number of pencils after the move
    remaining_pencils_move = initial_pencils - lost_pencils_move

    # Calculate the number of lost pencils due to poor pencil-keeping
    lost_pencils_poor_keeping = remaining_pencils_move / 3

    # Calculate the current number of pencils
    current_pencils = remaining_pencils_move - lost_pencils_poor_keeping

    # Display the current number of pencils
    result = current_pencils
    return result

print(solution())