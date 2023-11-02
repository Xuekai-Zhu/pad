def solution():
    blouse_time = 15  # in minutes
    dress_time = 20  # in minutes
    total_blouse_time = 2 * 60  # in minutes (2 hours)
    total_dress_time = 3 * 60  # in minutes (3 hours)

    # Calculate the total number of blouses ironed
    num_blouses = total_blouse_time // blouse_time

    # Calculate the total number of dresses ironed
    num_dresses = total_dress_time // dress_time

    # Calculate the total number of clothes ironed
    total_clothes = num_blouses + num_dresses
    result = total_clothes
    return result

print(solution())