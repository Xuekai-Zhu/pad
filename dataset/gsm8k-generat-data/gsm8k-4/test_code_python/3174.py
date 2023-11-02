def solution():
    """There were 30 women and 20 men who attended the party. After few hours, 2/5 of the total number of people left. If 9 men left the party, how many more women stayed at the party than men?"""
    # Define the initial number of women and men
    initial_women = 30
    initial_men = 20

    # Calculate the total number of people at the party
    total_people = initial_women + initial_men

    # Calculate the number of people who left the party
    people_left = total_people * 2/5

    # Calculate the number of men who left the party
    men_left = 9

    # Calculate the number of women who left the party
    women_left = people_left - men_left

    # Calculate the number of women and men who stayed at the party
    women_stayed = initial_women - women_left
    men_stayed = initial_men - men_left

    # Calculate the difference between the number of women and men who stayed at the party
    difference = abs(women_stayed - men_stayed)

    result = difference
    return result

print(solution())