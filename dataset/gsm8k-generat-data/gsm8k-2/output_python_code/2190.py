def solution():
    """There were 15 males and 10 more girls at the party. Each attendee received 2 cans of soft drinks. If Mary bought several boxes of soft drinks where a box contains 8 cans and is priced at $5 for each box, how much did Mary spend on soft drinks?"""
    males = 15
    girls = males + 10
    total_attendees = males + girls
    cans_needed = total_attendees * 2
    boxes_needed = cans_needed // 8 + (cans_needed % 8 > 0)
    price_per_box = 5
    total_cost = boxes_needed * price_per_box
    result = total_cost
    return result

print(solution())