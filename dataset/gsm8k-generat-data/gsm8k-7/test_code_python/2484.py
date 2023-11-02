def solution():
    num_people_1st_row = 24
    num_people_2nd_row = 20
    num_people_3rd_row = 18

    # Subtract the number of people who got up from the first row
    num_people_1st_row -= 3

    # Add the number of people who joined from the second row
    num_people_1st_row += 5

    # Calculate the total number of people left on the beach
    total_people_left = num_people_1st_row + num_people_2nd_row + num_people_3rd_row
    result = total_people_left
    return result

print(solution())