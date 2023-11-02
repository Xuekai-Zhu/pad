def solution():
    # Calculate the total number of students and chaperones
    total_people = (109 + 4*2) + (115 + 4*2) + (118 + 4*2)  # 4 teachers and 2 parents from each grade
    # Calculate the number of buses needed, rounded up to the nearest whole number
    buses_needed = (total_people-1) // 72 + 1  # the -1 is to account for the first bus being partially filled
    result = buses_needed
    return result

print(solution())