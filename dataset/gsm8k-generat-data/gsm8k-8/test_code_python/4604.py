def solution():
    # Calculate the number of girls on the trip
    boys_count = 50
    girls_count = (2 / 5) * boys_count + boys_count

    # Calculate the total number of people on the bus
    total_people_count = boys_count + girls_count + 2   # teacher + driver + assistant

    result = total_people_count
    return result

print(solution())