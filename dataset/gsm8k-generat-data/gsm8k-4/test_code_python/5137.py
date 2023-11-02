def solution():
    """Stoney Hollow Middle School is taking a field trip to the zoo. There are 109 fifth graders, 115 sixth graders, and 118 seventh graders. There are 4 teachers and 2 parents from each grade coming along to chaperone on the trip. There are 72 seats on each school bus. How many buses are needed for the field trip?"""
    # Define the number of students and chaperones for each grade
    fifth_grade = 109 + 4 + 2
    sixth_grade = 115 + 4 + 2
    seventh_grade = 118 + 4 + 2

    # Calculate the total number of people going on the trip
    total_people = fifth_grade + sixth_grade + seventh_grade

    # Calculate the number of buses needed, rounding up to the nearest whole number
    buses_needed = math.ceil(total_people / 72)

    # return the result
    result = buses_needed
    return result

print(solution())