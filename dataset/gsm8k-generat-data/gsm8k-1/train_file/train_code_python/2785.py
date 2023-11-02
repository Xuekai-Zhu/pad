def solution():
    """Tom decided to go on a trip. During this trip, he needs to cross a lake, which in one direction takes 4 hours. During this time, Tom needs an assistant to help him with the crossing. Hiring an assistant costs $10 per hour. How much would Tom have to pay for help with crossing the lake back and forth?"""
    crossing_time = 4
    assistant_cost = 10
    round_trip_time = crossing_time * 2
    cost_per_round_trip = round_trip_time * assistant_cost
    result = cost_per_round_trip
    return result

print(solution())