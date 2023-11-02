def solution():
    total_students = 180
    deaf_population = 3
    blind_population = 1

    # Set up system of equations to solve for number of blind students
    # deaf_population + blind_population = total_students
    # deaf_population = 3 * blind_population
    # Substitute first equation into second equation and solve for blind_population
    blind_population = total_students / (deaf_population + blind_population)
    # Calculate number of blind students
    num_blind_students = blind_population * blind_population
    result = num_blind_students
    return result

print(solution())