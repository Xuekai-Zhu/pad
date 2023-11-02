def solution():
    total_turtles = 60
    happy_island_turtles = total_turtles
    lonely_island_turtles = (happy_island_turtles - 10) / 2
    result = lonely_island_turtles
    return result

print(solution())