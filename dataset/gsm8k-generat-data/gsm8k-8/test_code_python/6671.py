def solution():
    # Define the total number of attendees
    total_attendees = 100

    # Calculate the number of women and men
    num_women = 0.5 * total_attendees
    num_men = 0.35 * total_attendees

    # Calculate the number of children
    num_children = total_attendees - num_women - num_men
    result = num_children
    return result

print(solution())