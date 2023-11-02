def solution():
    """Stoney Hollow Middle School is taking a field trip to the zoo. There are 109 fifth graders, 115 sixth graders, and 118 seventh graders. There are 4 teachers and 2 parents from each grade coming along to chaperone on the trip. There are 72 seats on each school bus. How many buses are needed for the field trip?"""
    # Define the number of students and chaperones from each grade
    fifth_graders = 109
    sixth_graders = 115
    seventh_graders = 118
    teachers_per_grade = 4
    parents_per_grade = 2

    # Calculate the total number of students and chaperones
    total_students = fifth_graders + sixth_graders + seventh_graders
    total_chaperones = (teachers_per_grade + parents_per_grade) * 3

    # Calculate the total number of people going on the trip
    total_people = total_students + total_chaperones

    # Calculate the number of buses needed
    buses_needed = total_people // 72 + (total_people % 72 > 0)

    # Display the number of buses needed
    result = buses_needed
    return result

print(solution())