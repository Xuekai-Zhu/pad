def solution():
    """Brian goes fishing twice as often as Chris, but catches 2/5 times fewer fish than Chris per trip. If Brian caught 400 fish every time he went fishing, how many fish did they catch altogether if Chris went fishing 10 times?"""
    # Define the number of times Brian went fishing
    brian_trips = 20  # Brian goes twice as often as Chris, so if Chris went 10 times, Brian went 20 times

    # Define the number of fish Brian catches per trip
    brian_catch_per_trip = 400

    # Define the number of fish Chris catches per trip
    chris_catch_per_trip = brian_catch_per_trip * (5/3)  # Brian catches 2/5 times fewer fish than Chris per trip

    # Calculate the total number of fish caught by Brian
    brian_total_catch = brian_trips * brian_catch_per_trip

    # Calculate the total number of fish caught by Chris
    chris_total_catch = 10 * chris_catch_per_trip

    # Calculate the total number of fish caught by both of them
    total_catch = brian_total_catch + chris_total_catch

    # return the result
    result = total_catch
    return result

print(solution())