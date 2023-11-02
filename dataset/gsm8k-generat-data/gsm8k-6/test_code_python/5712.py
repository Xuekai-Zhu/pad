def solution():
    # Calculate the total number of passengers the airline can accommodate each day
    total_seats = 5 * 20 * 7  # 5 airplanes, 20 rows each with 7 seats
    daily_capacity = total_seats * 2  # each airplane makes 2 flights a day
    result = daily_capacity
    return result

print(solution())