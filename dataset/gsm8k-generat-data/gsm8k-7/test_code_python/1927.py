def solution():
    # Mike's printing calculations
    mike_speed_before_break = 600
    mike_hours_before_break = 9
    mike_speed_after_break = mike_speed_before_break / 3
    mike_hours_after_break = 2

    mike_total_pamphlets_before_break = mike_speed_before_break * mike_hours_before_break
    mike_total_pamphlets_after_break = mike_speed_after_break * mike_hours_after_break
    mike_total_pamphlets = mike_total_pamphlets_before_break + mike_total_pamphlets_after_break

    # Leo's printing calculations
    leo_speed = mike_speed_before_break * 2
    leo_hours = mike_hours_before_break / 3

    leo_total_pamphlets = leo_speed * leo_hours

    # Total pamphlets printed
    total_pamphlets = mike_total_pamphlets + leo_total_pamphlets
    result = total_pamphlets
    return result

print(solution())