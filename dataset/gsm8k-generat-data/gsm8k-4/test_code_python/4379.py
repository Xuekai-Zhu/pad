def solution():
    """Jeremy is driving 600 miles to visit his parents. His average speed for this trip is 50 miles per hour. Every two hours of driving, he makes a rest stop for 15 minutes. His car gets 18 miles per gallon of gas, and his gas indicator comes on when he's used 15 gallons, at which point he stops to refill, which takes 10 minutes. How long, in minutes, does he take to get to his parents' house, if he starts out with a full tank of gas?"""
    # Define the distance and average speed of the trip
    distance = 600
    average_speed = 50

    # Calculate the total driving time, including rest stops
    driving_time = distance / average_speed
    rest_stops = (driving_time // 2) * 15
    total_time = driving_time + rest_stops

    # Calculate the number of refills needed and the time taken for refilling
    refills = distance / 18 / 15
    refill_time = refills * 10

    # Calculate the total time of the trip, including refilling
    total_time += refill_time

    # Convert the time to minutes and return the result
    result = total_time * 60
    return result.

print(solution())