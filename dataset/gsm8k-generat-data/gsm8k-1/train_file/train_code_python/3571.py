def solution():
    """Eliza can iron a blouse in 15 minutes and a dress in 20 minutes. If she spends 2 hours ironing blouses and 3 hours ironing dresses, how many pieces of clothes did she iron? """
    blouse_time = 15
    dress_time = 20
    total_blouse_time = 2*60
    total_dress_time = 3*60
    num_blouses = total_blouse_time/blouse_time
    num_dresses = total_dress_time/dress_time
    total_pieces = num_blouses + num_dresses
    result = total_pieces
    return result

print(solution())