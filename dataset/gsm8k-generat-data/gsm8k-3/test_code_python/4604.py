def solution():
    """On a trip to visit the local museum, Mr. Gordon has taken 2/5 times more girls than boys. If their bus has a driver and an assistant, and the total number of boys on the trip is 50, calculate the total number of people on the bus considering the teacher also drives together with the students on the bus."""
    # Calculate the number of girls based on the number of boys
    girls = (2/5) * 50 + 50

    # Calculate the total number of people including the driver and assistant
    total = girls + 50 + 2

    # Display the total number of people
    result = total
    return result

print(solution())