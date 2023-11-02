def solution():
    """Finley took part in a 100-meter race. She started off in first, but then fell back 5 spots. She then moved ahead 2 spots, before falling behind 3. Lastly, she jumped ahead 1 spot to finish the race. What place did she finish in?"""
    starting_position = 1
    fallen_back = 5
    moved_ahead = 2
    fallen_behind = 3
    jumped_ahead = 1
    final_position = (starting_position - fallen_back + moved_ahead - fallen_behind + jumped_ahead)
    result = final_position
    return result

print(solution())