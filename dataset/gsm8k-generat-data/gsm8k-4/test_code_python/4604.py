def solution():
    """On a trip to visit the local museum, Mr. Gordon has taken 2/5 times more girls than boys. If their bus has a driver and an assistant, and the total number of boys on the trip is 50, calculate the total number of people on the bus considering the teacher also drives together with the students on the bus."""
    # Define the ratio of girls to boys
    ratio = 2/5

    # Calculate the number of girls
    girls = ratio * 50

    # Calculate the total number of students
    students = girls + 50

    # Add the driver, the assistant, and the teacher to get the total number of people on the bus
    total_people = students + 3

    # return the result
    result = total_people
    return result

print(solution())