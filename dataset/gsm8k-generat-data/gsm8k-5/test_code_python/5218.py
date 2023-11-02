def solution():
    # Brian catches 2/5 times fewer fish than Chris per trip
    brian_catches = 3/5  # Brian catches 3/5 as many fish as Chris per trip
    chris_catches = 1  # Chris catches 1 as many fish as Chris per trip

    # Brian goes fishing twice as often as Chris
    brian_frequency = 2
    chris_frequency = 1

    # If Brian caught 400 fish every time he went fishing,
    brian_catch_per_trip = 400
    chris_catch_per_trip = int(brian_catch_per_trip * (1/brian_catches) * (1/chris_frequency) * (1/brian_frequency))

    # Chris went fishing 10 times
    chris_trips = 10
    total_catch = chris_trips * chris_catch_per_trip + brian_frequency * (chris_trips * brian_catch_per_trip)

    result = total_catch
    return result

print(solution())