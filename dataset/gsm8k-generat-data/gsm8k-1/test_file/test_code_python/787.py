def solution():
    """A train has 172 people traveling on it. At the first stop 47 people get off and 13 more people get on, and at the next stop another 38 people get off. How many people are on the train?"""
    initial_passengers = 172
    passengers_off = 47 + 38
    passengers_on = 13
    total_passengers = initial_passengers - passengers_off + passengers_on
    result = total_passengers
    return result

print(solution())