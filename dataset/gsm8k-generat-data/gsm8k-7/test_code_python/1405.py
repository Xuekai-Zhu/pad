def solution():
    num_boys = 16
    num_girls = 14

    # Calculate the number of boys and girls who brought gifts
    boys_with_gifts = (3/4) * num_boys
    girls_with_gifts = (6/7) * num_girls

    # Calculate the total number of attendees who brought gifts
    total_with_gifts = boys_with_gifts + girls_with_gifts

    # Calculate the number of attendees who did not bring gifts
    total_attendees = num_boys + num_girls
    no_gifts = total_attendees - total_with_gifts
    result = no_gifts
    return result

print(solution())