def solution():
    oysters_per_5_minutes = 10
    minutes_per_hour = 60

    # Calculate the total number of oysters Bob can shuck in one hour
    oysters_per_hour = (oysters_per_5_minutes / 5) * minutes_per_hour

    # Calculate the total number of oysters Bob can shuck in two hours
    oysters_in_two_hours = oysters_per_hour * 2

    result = oysters_in_two_hours
    return result

print(solution())