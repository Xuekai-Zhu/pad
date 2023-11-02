def solution():
    
    # Define the number of pies and pieces per pie
    num_pies = 5
    pieces_per_pie = 8

    # Calculate the total number of pieces
    total_pieces = num_pies * pieces_per_pie

    # Subtract the number of pies given out on the buffet table
    total_pieces -= 5

    # Subtract the number of pie remaining
    total_pieces -= 14

    # Display the number of pieces taken by the guests
    result = total_pieces
    return result

print(solution())