def solution():
    # Calculate the total number of seats on the bus
    total_seats = 23 * 4  

    # Calculate the number of people on the bus after the first stop
    people_on_bus = 16 + 15 - 3  

    # Calculate the number of people on the bus after the second stop
    people_on_bus = people_on_bus + 17 - 10  

    # Calculate the number of empty seats on the bus after the second stop
    empty_seats = total_seats - people_on_bus  
    result = empty_seats
    return result

print(solution())