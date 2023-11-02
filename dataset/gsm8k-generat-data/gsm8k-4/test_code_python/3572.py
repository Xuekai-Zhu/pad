def solution():
    """Eliza can iron a blouse in 15 minutes and a dress in 20 minutes.  If she spends 2 hours ironing blouses and 3 hours ironing dresses, how many pieces of clothes did she iron?"""
    # Define the time it takes to iron a single blouse and dress
    blouse_time = 15
    dress_time = 20

    # Calculate the total time spent ironing blouses and dresses
    total_time = (2 * 60) + (3 * 60)

    # Calculate the total number of blouses and dresses ironed
    blouses = total_time // blouse_time
    dresses = total_time // dress_time

    # Return the total number of pieces of clothing ironed
    result = blouses + dresses
    return result

print(solution())