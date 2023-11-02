def solution():
    # Calculate the number of girls on the trip
    boys = 50
    girls = (2/5) * boys + boys

    # Calculate the total number of people on the bus
    total_people = boys + girls + 2  # 2 is added for the driver and assistant
    result = total_people
    return result

print(solution())