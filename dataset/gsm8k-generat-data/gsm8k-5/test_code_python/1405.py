def solution():
    boys = 16  # Number of boys at the party
    girls = 14  # Number of girls at the party

    # Calculate number of boys and girls who brought gifts
    boys_with_gifts = 3/4 * boys
    girls_with_gifts = 6/7 * girls

    # Calculate total number of attendees who brought gifts
    total_with_gifts = boys_with_gifts + girls_with_gifts

    # Calculate number of attendees who did not bring gifts
    total_attendees = boys + girls
    total_without_gifts = total_attendees - total_with_gifts

    result = total_without_gifts
    return result

print(solution())