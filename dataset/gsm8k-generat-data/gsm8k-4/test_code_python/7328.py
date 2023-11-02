def solution():
    """A fifth-grade class went on a field trip to the zoo, and their class of 10 students merged with another class with the same amount of students. 5 parents offered to be a chaperone, and 2 of the teachers from both classes will be there too. When the school day was over, the students could choose to go home and 10 of them left. Two of the chaperones were parents in that group, so they left as well. How many individuals were left at the zoo?"""
    # Define the initial number of students
    initial_students = 10

    # Calculate the total number of individuals at the zoo
    total_individuals = initial_students * 2 + 5 + 2

    # Calculate the number of individuals who left
    individuals_left = 10 + 2

    # Calculate the number of chaperones left
    chaperones_left = 5 - 2

    # Calculate the number of individuals who are still at the zoo
    individuals_at_zoo = total_individuals - individuals_left - chaperones_left

    # return the result
    result = individuals_at_zoo
    return result

print(solution())