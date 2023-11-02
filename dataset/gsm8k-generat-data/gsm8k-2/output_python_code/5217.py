def solution():
    """Brian goes fishing twice as often as Chris, but catches 2/5 times fewer fish than Chris per trip. If Brian caught 400 fish every time he went fishing, how many fish did they catch altogether if Chris went fishing 10 times?"""
    chris_trips = 10
    brian_trips = 2 * chris_trips
    brian_catch_per_trip = 400
    chris_catch_per_trip = brian_catch_per_trip * (5/3)
    total_catch = (brian_trips * brian_catch_per_trip) + (chris_trips * chris_catch_per_trip)
    result = total_catch
    return result

print(solution())