def solution():
    """There is a very large room that has 4 tables, 1 sofa and 2 chairs that have 4 legs each. There are also 3 tables with 3 legs each, 1 table with 1 leg, and 1 rocking chair with 2 legs. How many legs are there in the room?"""
    leg_count = 0
    leg_count += 4 * 4  # 4 tables with 4 legs each
    leg_count += 1 * 4  # 1 sofa with 4 legs
    leg_count += 2 * 4  # 2 chairs with 4 legs each
    leg_count += 3 * 3  # 3 tables with 3 legs each
    leg_count += 1 * 1  # 1 table with 1 leg
    leg_count += 1 * 2  # 1 rocking chair with 2 legs
    result = leg_count
    return result

print(solution())