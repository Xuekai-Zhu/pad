def solution():
    """One hundred people attended a party. Fifty percent of the attendees are women, thirty-five percent of them are men, and the rest are children. How many children attended the party?"""
    # Define the total number of attendees
    total_attendees = 100

    # Calculate the number of women and men
    women = total_attendees * 0.5
    men = total_attendees * 0.35

    # Calculate the number of children
    children = total_attendees - women - men

    # Display the number of children
    result = children
    return result

print(solution())