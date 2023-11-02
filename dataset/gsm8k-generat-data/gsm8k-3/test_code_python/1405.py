def solution():
    """Sixteen boys and 14 girls attended Simon's birthday party. Three-fourths of the boys and 6/7 of the girls brought gifts. How many of those who attended did not bring gifts?"""
    # Calculate the number of boys who brought gifts
    boys_with_gifts = int(0.75 * 16)

    # Calculate the number of girls who brought gifts
    girls_with_gifts = int((6/7) * 14)

    # Calculate the total number of attendees who brought gifts
    total_with_gifts = boys_with_gifts + girls_with_gifts

    # Calculate the number of attendees who did not bring gifts
    total_attendees = 16 + 14
    attendees_without_gifts = total_attendees - total_with_gifts

    # Display the number of attendees who did not bring gifts
    result = attendees_without_gifts
    return result

print(solution())