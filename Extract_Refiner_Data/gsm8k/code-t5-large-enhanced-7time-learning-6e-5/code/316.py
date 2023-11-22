def solution():
    
    # Define the initial number of men and women
    initial_men = 25
    initial_women = 15

    # Calculate the total number of people at the party
    total_people = initial_men + initial_women

    # Calculate the number of people who left after an hour
    people_left = total_people / 4

    # Calculate the number of women left after the party's stay
    women_left = people_left - 22

    # Display the number of women left
    result = women_left
    return result

print(solution())