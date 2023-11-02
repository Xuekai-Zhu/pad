def solution():
    """Sixteen boys and 14 girls attended Simon's birthday party. Three-fourths of the boys and 6/7 of the girls brought gifts. How many of those who attended did not bring gifts?"""
    # Define the number of boys and girls
    num_boys = 16
    num_girls = 14

    # Calculate the number of boys and girls who brought gifts
    num_boys_with_gifts = int(num_boys * (3/4))
    num_girls_with_gifts = int(num_girls * (6/7))

    # Calculate the total number of attendees with gifts
    total_with_gifts = num_boys_with_gifts + num_girls_with_gifts

    # Calculate the number of attendees who did not bring gifts
    total_attendees = num_boys + num_girls
    num_without_gifts = total_attendees - total_with_gifts

    result = num_without_gifts
    return result

print(solution())