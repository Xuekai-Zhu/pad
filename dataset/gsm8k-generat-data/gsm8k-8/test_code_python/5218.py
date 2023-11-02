def solution():
    # Define the number of times Chris went fishing
    chris_trips = 10

    # Calculate the number of times Brian went fishing
    brian_trips = 2 * chris_trips

    # Calculate the number of fish Chris caught per trip
    chris_catch = 400 / (1 - 2/5)

    # Calculate the total number of fish Chris caught
    chris_total_catch = chris_trips * chris_catch

    # Calculate the total number of fish Brian caught
    brian_total_catch = brian_trips * 400

    # Calculate the overall total catch
    total_catch = chris_total_catch + brian_total_catch
    result = total_catch
    return result

print(solution())