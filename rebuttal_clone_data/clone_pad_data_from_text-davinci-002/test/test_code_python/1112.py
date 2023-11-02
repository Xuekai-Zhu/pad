def solution():
    paper_boats = 30
    eaten_boats = paper_boats * 0.2
    shot_boats = 2
    remaining_boats = paper_boats - eaten_boats - shot_boats
    result = remaining_boats
    return result

print(solution())