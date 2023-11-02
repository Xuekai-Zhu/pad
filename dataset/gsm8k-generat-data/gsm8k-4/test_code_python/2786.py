def solution():
    """Tom decided to go on a trip. During this trip, he needs to cross a lake, which in one direction takes 4 hours. During this time, Tom needs an assistant to help him with the crossing. Hiring an assistant costs $10 per hour. How much would Tom have to pay for help with crossing the lake back and forth?"""
    # Define the time it takes to cross the lake in one direction
    time_one_way = 4

    # Calculate the total time it takes to cross the lake back and forth
    time_round_trip = time_one_way * 2

    # Calculate the cost of hiring an assistant for the entire round trip
    cost = time_round_trip * 10

    result = cost
    return result

print(solution())