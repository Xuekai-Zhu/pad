def solution():
    
    # Define the initial number of gum pieces
    gum_pieces = 20

    # Calculate the number of gum pieces Jim chews on the way home from school
    gum_pieces -= 2

    # Calculate the number of gum pieces Jim chews stick after dinner
    gum_pieces -= 1

    # Calculate the number of gum pieces Jim gives to his sister
    gum_pieces *= 0.5

    # Calculate the number of gum pieces Jim has left at the end of the day
    gum_pieces_left = gum_pieces - gum_pieces

    # Display the number of gum pieces Jim has left at the end of the day
    result = gum_pieces_left
    return result

print(solution())