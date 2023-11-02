def solution():
    sarah_speeding_tickets = 6

    # Since they each have an equal number of speeding tickets and Sarah has 6,
    # we know that Mark also has 6 speeding tickets
    mark_speeding_tickets = 6

    # Mark has twice as many parking tickets as Sarah, so we can calculate how many
    # parking tickets Sarah has and then double that to find Mark's total
    sarah_parking_tickets = (24 - sarah_speeding_tickets - mark_speeding_tickets) / 3
    mark_parking_tickets = sarah_parking_tickets * 2

    result = mark_parking_tickets
    return result

print(solution())