def solution():
    """A woodworker is crafting enough furniture legs for their projects. They have made a total of 40 furniture legs so far, and this is the exact amount they needed for everything they’re building. If the woodworker is using these legs for their tables and chairs and they have built 6 chairs, how many tables have they made?"""
    total_legs = 40
    legs_per_chair = 4
    legs_per_table = 4
    total_chairs = 6
    total_legs_used = total_chairs * legs_per_chair
    legs_remaining = total_legs - total_legs_used
    tables_with_legs = legs_remaining // legs_per_table
    result = tables_with_legs
    return result

print(solution())