def solution():
    # Calculate the number of girls at the beginning of the academic year
    num_girls = int(15 * 1.2)  # 20% more girls than boys

    # Calculate the total number of students at the beginning of the year
    total_students = num_girls + 15  # 15 boys and the number of girls calculated above

    # Calculate the number of girls after transfer students were admitted
    num_girls += num_girls  # double the number of girls

    # Calculate the total number of students after transfer students were admitted
    total_students = num_girls + 15  # 15 boys and the updated number of girls

    result = total_students
    return result

print(solution())