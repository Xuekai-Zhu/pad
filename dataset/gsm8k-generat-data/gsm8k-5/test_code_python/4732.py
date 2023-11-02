def solution():
    distance = 500  # The distance of the rowboat race is 500 yards
    speed_biff = 50 / 60  # Biff rows at 50 yards per minute
    speed_kenneth = 51 / 60  # Kenneth rows at 51 yards per minute

    # Calculate the time it takes for Biff and Kenneth to cross the finish line
    time_biff = distance / speed_biff
    time_kenneth = distance / speed_kenneth

    # Calculate the distance Kenneth will be past the finish line when Biff crosses it
    distance_past_finish = abs((time_biff * speed_kenneth) - distance)
    result = distance_past_finish
    return result

print(solution())