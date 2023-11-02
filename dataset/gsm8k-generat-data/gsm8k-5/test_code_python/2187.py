def solution():
    # Calculate the total age of 9 students
    total_age = 9 * 8

    # Calculate the new total age if the tenth student is added
    new_total_age = total_age + 28

    # Calculate the new average age
    new_average_age = new_total_age / 10

    # Calculate the increase in average age
    increase = new_average_age - 8
    result = increase
    return result

print(solution())