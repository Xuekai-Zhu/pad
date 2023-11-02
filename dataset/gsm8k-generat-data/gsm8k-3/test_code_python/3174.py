def solution():
    """There were 30 women and 20 men who attended the party. After few hours, 2/5 of the total number of people left. If 9 men left the party, how many more women stayed at the party than men?"""
    # Initialize the number of women and men
    women = 30
    men = 20

    # Calculate the total number of people at the party
    total_people = women + men

    # Calculate the number of people who left the party
    left_people = total_people * (2/5)

    # Calculate the number of women who left the party
    left_women = left_people * (women / total_people)

    # Calculate the number of men who left the party
    left_men = left_people * (men / total_people)

    # Calculate the number of women who stayed at the party
    stayed_women = women - left_women

    # Calculate the number of men who stayed at the party
    stayed_men = men - 9

    # Calculate the difference between the number of women and men who stayed at the party
    difference = stayed_women - stayed_men

    # Display the difference
    result = difference
    return result

print(solution())