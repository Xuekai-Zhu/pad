def solution():
    # Calculate the total number of students and chaperones
    total_students = 109 + 115 + 118  # 109 fifth graders, 115 sixth graders, and 118 seventh graders
    total_chaperones = (4 + 2) * 3  # There are 4 teachers and 2 parents from each grade coming along

    # Calculate the total number of people going on the trip
    total_people = total_students + total_chaperones

    # Calculate the number of buses needed
    buses_needed = total_people // 72 + (total_people % 72 > 0)  # Round up to the nearest whole number

    result = buses_needed
    return result

print(solution())