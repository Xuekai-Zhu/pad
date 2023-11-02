def solution():
    """Eliza can iron a blouse in 15 minutes and a dress in 20 minutes. If she spends 2 hours ironing blouses and 3 hours ironing dresses, how many pieces of clothes did she iron?"""
    blouse_time = 15
    dress_time = 20
    blouse_hours = 2
    dress_hours = 3

    total_blouses = (blouse_hours * 60) // blouse_time
    total_dresses = (dress_hours * 60) // dress_time
    total_clothes = total_blouses + total_dresses

    result = total_clothes
    return result

print(solution())