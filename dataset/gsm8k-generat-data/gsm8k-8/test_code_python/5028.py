def solution():
    # Define the variables
    one_person_time = 10
    one_person_productivity = 1
    total_productivity = 2

    # Calculate the new time with two people
    two_people_time = one_person_time * one_person_productivity / total_productivity
    result = two_people_time
    return result

print(solution())