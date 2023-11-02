def solution():
    # Calculate the total number of videos Billy watches
    total_watched = 15 * 5

    # Add 1 for the extra video Billy watched before finding one he liked
    total_watched += 1

    # Calculate the number of videos in the final suggestion list before Billy chose the 5th one
    final_list_length = 15 ** 5

    # Subtract the number of videos in the final suggestion list from the total watched to find the number Billy didn't watch
    not_watched = final_list_length - total_watched

    # Add 5 to represent the video Billy chose from the final suggestion list
    watched = total_watched + 5
    result = watched
    return result

print(solution())