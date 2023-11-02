def solution():
    # Define the initial number of women and men
    initial_women = 30
    initial_men = 20

    # Calculate the total number of people
    total_people = initial_women + initial_men

    # Calculate the number of people who left the party
    left_people = 2/5 * total_people

    # Calculate the number of women and men who left the party
    left_women = left_people / 2
    left_men = left_people / 2 - 9

    # Calculate the number of women and men who stayed at the party
    stayed_women = initial_women - left_women
    stayed_men = initial_men - left_men

    # Calculate the difference between the number of women and men who stayed
    diff = stayed_women - stayed_men
    result = diff
    return result

print(solution())