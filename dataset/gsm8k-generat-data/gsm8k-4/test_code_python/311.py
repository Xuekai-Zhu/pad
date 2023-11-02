def solution():
    """The seats of a bus are arranged in 23 rows of 4 seats. At the start, 16 people climb. At the first stop, 15 people board the bus and 3 get off. At the second stop, 17 people get on the bus and 10 get off. How many empty seats are there after the second stop?"""
    # Define the number of rows and seats per row
    ROWS = 23
    SEATS_PER_ROW = 4

    # Calculate the total number of seats on the bus
    total_seats = ROWS * SEATS_PER_ROW

    # Calculate the number of people on the bus after the initial climb
    people_on_bus = 16

    # Calculate the number of people boarding and getting off at the first stop
    people_boarded_1 = 15
    people_getting_off_1 = 3

    # Calculate the number of people on the bus after the first stop
    people_on_bus = people_on_bus + people_boarded_1 - people_getting_off_1

    # Calculate the number of people boarding and getting off at the second stop
    people_boarded_2 = 17
    people_getting_off_2 = 10

    # Calculate the number of people remaining on the bus after the second stop
    people_on_bus = people_on_bus + people_boarded_2 - people_getting_off_2

    # Calculate the number of empty seats on the bus
    empty_seats = total_seats - people_on_bus

    result = empty_seats
    return result

print(solution())