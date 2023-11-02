def solution():
    """There are 10 students in a class. The average age of 9 of them is 8 years. By how many years will this average increase if the tenth student is (quite strangely) 28 years old?"""
    # Define the number of students and the initial average age
    num_students = 10
    initial_avg_age = 8

    # Calculate the sum of the ages of the first 9 students
    sum_ages = initial_avg_age * (num_students - 1)

    # Add the age of the tenth student
    sum_ages += 28

    # Calculate the new average age
    new_avg_age = sum_ages / num_students

    # Calculate how much the average age increased
    increase = new_avg_age - initial_avg_age

    # Display the increase in average age
    result = increase
    return result

print(solution())