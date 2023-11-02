def solution():
    boys = 50  # The total number of boys on the trip is 50
    girls = (2/5) * boys + boys  # Mr. Gordon took 2/5 times more girls than boys
    bus_staff = 2  # The bus has a driver and an assistant

    # Calculate the total number of people on the bus, including Mr. Gordon and the students
    total_people = boys + girls + bus_staff + 1  # Mr. Gordon is also on the bus, so add 1 to the total

    result = total_people
    return result

print(solution())