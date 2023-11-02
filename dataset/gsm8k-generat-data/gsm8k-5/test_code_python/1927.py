def solution():
    # Pamphlets printed by Mike before his break
    mike_before_break = 600 * 9

    # Pamphlets printed by Mike after his break
    mike_after_break = 600 / 3 * 2

    # Total pamphlets printed by Mike
    mike_total = mike_before_break + (mike_after_break * 2)

    # Pamphlets printed by Leo
    leo_hours = 9 / 3
    leo_speed = 600 * 2
    leo_total = leo_hours * leo_speed

    # Total pamphlets printed by both
    total_pamphlets = mike_total + leo_total
    result = total_pamphlets
    return result

print(solution())