def solution():
    # Calculate the number of hours James writes per night
    hours_per_night = 4 - 1

    # Calculate the number of pages James writes per night
    pages_per_night = hours_per_night * 5

    # Calculate the number of nights it will take to finish the book
    nights_to_finish = 735 / pages_per_night

    # Calculate the number of weeks it will take to finish the book, rounding up to the nearest integer
    weeks_to_finish = math.ceil(nights_to_finish / 7)

    result = weeks_to_finish
    return result

print(solution())