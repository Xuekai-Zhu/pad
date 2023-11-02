def solution():
    """A three-ounce box of flavored jello makes 10 small jello cups. Greg wants to make small jello cups for his son's outdoor birthday party. There will be 30 kids and he wants to have enough so that each kid can have 4 jello cups. Jello is currently on sale for $1.25. How much will he spend on jello?"""
    jello_ounces_per_box = 3
    cups_per_box = 10
    kids_at_party = 30
    cups_per_kid = 4
    total_cups_needed = kids_at_party * cups_per_kid
    boxes_needed = total_cups_needed / cups_per_box
    jello_cost_per_box = 1.25
    total_cost = boxes_needed * jello_cost_per_box
    result = total_cost
    return result

print(solution())