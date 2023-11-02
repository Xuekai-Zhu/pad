def solution():
    num_flights = 3
    flight_height = 10
    rope_height = flight_height / 2
    ladder_height = rope_height + 10

    # Calculate the total height John climbed
    total_height = (num_flights * flight_height) + rope_height + ladder_height
    result = total_height
    return result

print(solution())