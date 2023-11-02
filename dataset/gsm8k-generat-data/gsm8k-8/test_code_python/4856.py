def solution():
    # Each person has 2 feet, and each foot has a skate with 4 wheels
    num_wheels_per_person = 2 * 4

    # Multiply the number of people by the number of wheels per person to get the total number of wheels
    total_wheels = num_wheels_per_person * 40
    result = total_wheels
    return result

print(solution())