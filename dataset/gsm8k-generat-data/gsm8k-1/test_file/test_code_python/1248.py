def solution():
    """Dominick went to his team's changing room and saw half as many robots as helmets and half as many helmets as footballs kept there. If there were 20 helmets, calculate the total number of items Dominick saw."""
    helmets = 20
    footballs = 2 * helmets
    robots = helmets / 2
    total_items = helmets + footballs + robots
    result = total_items
    return result

print(solution())