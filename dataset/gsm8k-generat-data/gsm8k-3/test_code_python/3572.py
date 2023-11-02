def solution():
    """Eliza can iron a blouse in 15 minutes and a dress in 20 minutes.  If she spends 2 hours ironing blouses and 3 hours ironing dresses, how many pieces of clothes did she iron?"""
    # Define the time taken to iron a blouse and a dress
    BLOUSE_TIME = 15
    DRESS_TIME = 20

    # Define the time taken to iron each type of clothing
    blouse_hours = 2
    dress_hours = 3

    # Calculate the number of blouses and dresses ironed
    blouses = (blouse_hours * 60) // BLOUSE_TIME
    dresses = (dress_hours * 60) // DRESS_TIME

    # Calculate the total number of pieces of clothing ironed
    total_pieces = blouses + dresses

    # Display the total number of pieces of clothing ironed
    result = total_pieces
    return result

print(solution())