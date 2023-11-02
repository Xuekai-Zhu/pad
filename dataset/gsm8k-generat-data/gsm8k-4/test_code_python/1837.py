def solution():
    """Mr. Langsley commutes to work every day by bus. The bus picks him up at 6:00 a.m. and takes forty minutes to arrive at the first station. If Mr. Langsley arrives at work at 9:00 a.m., what's the total time taken in minutes from the first station to Mr. Langsley's workplace?"""
    # Define the time the bus takes to travel from the first station to Mr. Langsley's workplace
    bus_travel_time = 120

    # Define the time between the bus arrival at the first station and Mr. Langsley's arrival at work
    total_time = bus_travel_time - 40

    return total_time

print(solution())