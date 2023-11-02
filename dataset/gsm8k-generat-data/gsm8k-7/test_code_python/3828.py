def solution():
    total_guests = 50
    num_women = total_guests / 2
    num_men = 15
    num_children = total_guests - num_women - num_men

    # Calculate the number of men who left
    num_men_left = num_men / 5

    # Calculate the number of children who left
    num_children_left = 4

    # Calculate the total number of guests who left
    total_guests_left = num_men_left + num_children_left

    # Calculate the total number of guests who stayed
    total_guests_stayed = total_guests - total_guests_left
    result = total_guests_stayed
    return result

print(solution())