def solution():
    # Define the total number of guests and the number of men
    total_guests = 50
    men = 15

    # Calculate the number of women and children
    women = total_guests / 2
    children = total_guests - (women + men)

    # Calculate the number of guests who left during the movie
    men_left = men / 5
    children_left = 4
    total_left = men_left + children_left

    # Calculate the number of guests who stayed until the end of the movie
    guests_stayed = total_guests - total_left

    result = guests_stayed
    return result

print(solution())