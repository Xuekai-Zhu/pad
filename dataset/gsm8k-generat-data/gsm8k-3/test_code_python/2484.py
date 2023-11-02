def solution():
    """There are 3 rows of people relaxing at the beach. The first row is made up of 24 people until 3 people get up to wade in the water. 5 people from the second row, which originally held 20 people, go to join them. The third row is made up of 18 people. How many people are left relaxing on the beach?"""
    # Calculate the number of people in the first row after some leave
    first_row = 24 - 3

    # Calculate the number of people in the second row after some leave
    second_row = 20 - 5

    # Calculate the total number of people left on the beach
    total_people = first_row + second_row + 18

    # Display the total number of people left on the beach
    result = total_people
    return result

print(solution())