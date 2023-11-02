def solution():
    # Calculate the total age of the 9 students
    total_age = 9 * 8  # average age of 9 students is 8 years

    # Calculate the new total age including the tenth student
    new_total_age = total_age + 28  # tenth student is 28 years old

    # Calculate the new average age of all 10 students
    new_average_age = new_total_age / 10

    # Calculate the increase in average age
    increase_in_average_age = new_average_age - 8  # original average age was 8 years

    result = increase_in_average_age
    return result

print(solution())