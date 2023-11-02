def solution():
    # Calculate the total number of students and chaperones
    total_students = 109 + 115 + 118
    total_chaperones = (4 + 2) * 3

    # Calculate the total number of people going on the trip
    total_people = total_students + total_chaperones

    # Calculate the number of buses needed
    buses_needed = total_people // 72 + (total_people % 72 > 0)

    result = buses_needed
    return result

print(solution())