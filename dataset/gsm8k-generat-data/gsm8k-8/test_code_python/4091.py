def solution():
    # Define the number of men and women in the office
    total_people = 0
    women_ratio = 0.5

    # Calculate the initial number of women in the office
    initial_women = total_people * women_ratio

    # Calculate the reduced number of women in the office after the meeting
    reduced_women = initial_women * 0.8

    # Calculate the total number of people in the office before the meeting
    total_people_before = 2 * initial_women

    # Calculate the total number of people in the office after the meeting
    total_people_after = total_people_before - 6 + 4

    # Return the total number of people in the office
    result = total_people_after
    return result

print(solution())