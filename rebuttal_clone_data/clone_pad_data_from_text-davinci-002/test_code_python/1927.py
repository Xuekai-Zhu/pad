def solution():
    mike_pamphlets_per_hour = 600
    leo_pamphlets_per_hour = mike_pamphlets_per_hour * 2
    mike_hours_before_break = 9
    leo_hours_before_break = mike_hours_before_break / 3
    mike_hours_after_break = 2
    leo_hours_after_break = mike_hours_after_break / 3
    mike_pamphlets_before_break = mike_pamphlets_per_hour * mike_hours_before_break
    leo_pamphlets_before_break = leo_pamphlets_per_hour * leo_hours_before_break
    mike_pamphlets_after_break = mike_pamphlets_before_break / 3
    leo_pamphlets_after_break = leo_pamphlets_before_break / 2
    total_mike_pamphlets = mike_pamphlets_before_break + mike_pamphlets_after_break

print(solution())