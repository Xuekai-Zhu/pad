def solution():
    
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