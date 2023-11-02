def solution():
    """Tom decided to go on a trip. During this trip, he needs to cross a lake, which in one direction takes 4 hours. During this time, Tom needs an assistant to help him with the crossing. Hiring an assistant costs $10 per hour. How much would Tom have to pay for help with crossing the lake back and forth?"""
    # Define the number of hours Tom needs an assistant for each direction
    ASSISTANT_HOURS = 4

    # Define the hourly rate for the assistant
    ASSISTANT_RATE = 10

    # Calculate the cost of hiring an assistant for one round trip
    round_trip_hours = ASSISTANT_HOURS * 2
    round_trip_cost = round_trip_hours * ASSISTANT_RATE

    # Display the total cost for help with crossing the lake back and forth
    result = round_trip_cost
    return result

print(solution())