def solution():
    """On a trip to visit the local museum, Mr. Gordon has taken 2/5 times more girls than boys. If their bus has a driver and an assistant, and the total number of boys on the trip is 50, calculate the total number of people on the bus considering the teacher also drives together with the students on the bus."""
    boys_on_trip = 50
    girls_on_trip = (2/5) * boys_on_trip + boys_on_trip
    total_people = boys_on_trip + girls_on_trip + 2
    # adding 2 for the driver and assistant
    result = total_people
    return result

print(solution())