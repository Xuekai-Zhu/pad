def solution():
    """There are 3 rows of people relaxing at the beach. The first row is made up of 24 people until 3 people get up to wade in the water. 5 people from the second row, which originally held 20 people, go to join them. The third row is made up of 18 people. How many people are left relaxing on the beach?"""
    # Define the initial number of people in each row
    row1 = 24
    row2 = 20
    row3 = 18

    # Subtract the number of people who got up from the first row
    row1 -= 3

    # Subtract the number of people who went to wade in the water from the second row
    row2 -= 5

    # Calculate the total number of people left on the beach
    total_people = row1 + row2 + row3

    # Return the result
    result = total_people
    return result

print(solution())