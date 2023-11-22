def solution():
    
    # Define the number of apple pies and the number of pieces per pie
    num_pies = 5
    pieces_per_pie = 8

    # Calculate the total number of pieces of pie
    total_pieces = num_pies * pieces_per_pie

    # Calculate the number of pieces of pie taken by the guests
    taken_pieces = total_pieces - 14

    # Display the number of pieces of pie taken
    result = taken_pieces
    return result

print(solution())