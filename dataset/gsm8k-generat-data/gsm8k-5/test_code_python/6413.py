def solution():
    num_students = 200  # Number of students who passed the course three years ago
    increase_percent = 0.5  # Each subsequent year, the number of students increases by 50% of the previous year
    current_year = 4  # We are currently in the fourth year

    # Calculate the number of students who passed the course in each subsequent year
    for year in range(1, current_year):
        num_students = num_students * (1 + increase_percent)

    result = int(num_students)
    return result

print(solution())