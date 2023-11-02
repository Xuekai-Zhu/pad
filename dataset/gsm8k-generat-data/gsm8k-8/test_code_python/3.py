def solution():
    # Define the number of pages Julie read yesterday and today
    yesterday = 12
    today = 2 * yesterday

    # Calculate the number of pages Julie has left to read
    pages_left = 120 - yesterday - today

    # Calculate the number of pages Julie needs to read tomorrow
    pages_tomorrow = pages_left / 2

    result = pages_tomorrow
    return result

print(solution())