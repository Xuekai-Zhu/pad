def solution():
    """On a trip to visit the local museum, Mr. Gordon has taken 2/5 times more girls than boys. If their bus has a driver and an assistant, and the total number of boys on the trip is 50, calculate the total number of people on the bus considering the teacher also drives together with the students on the bus."""
    boys = 50
    girls = (2/5) * boys + boys
    total_students = boys + girls
    total_people = total_students + 2
    result = total_people
    return result

print(solution())