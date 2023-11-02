def solution():
    # Calculate the total number of hours the spaceship traveled
    total_travel_hours = 72  # 3 days x 24 hours/day
    travel_hours_first_leg = 10 + 3  # 10 hours of travel, 3 hours of break
    travel_hours_second_leg = 10 + 1  # 10 hours of travel, 1 hour of break
    travel_hours_remaining = total_travel_hours - travel_hours_first_leg - travel_hours_second_leg
    travel_hours_remaining_with_break = travel_hours_remaining // 11 * 12  # 11 hours of travel, 1 hour of break

    # Calculate the total number of hours the spaceship was not moving
    total_break_hours = (total_travel_hours - travel_hours_first_leg - travel_hours_second_leg - travel_hours_remaining_with_break)

    result = total_break_hours
    return result

print(solution())