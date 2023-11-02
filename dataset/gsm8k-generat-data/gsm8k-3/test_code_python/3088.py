def solution():
    """Keanu's motorcycle can store 8 liters of gasoline. If his destination is 280 miles away and his motorcycle consumes 8 liters of gasoline per 40 miles, how many times does Keanu have to refill his motorcycle with gasoline if he will make a round trip?"""
    # Calculate the total distance of the round trip
    round_trip_distance = 280 * 2

    # Calculate the total amount of gasoline needed for the round trip
    total_gasoline = round_trip_distance / 40 * 8

    # Calculate the number of times Keanu needs to refill his motorcycle
    num_refills = total_gasoline / 8

    # Display the number of refills needed
    result = num_refills
    return result

print(solution())