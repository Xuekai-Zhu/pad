def solution():
    """To make a cherry pie, Veronica needs 3 pounds of pitted cherries. There are 80 single cherries in one pound of cherries. It takes 10 minutes to pit 20 cherries. How many hours will it take Veronica to pit all the cherries?"""
    cherries_needed = 3 * 80
    cherries_pitted_per_round = 20
    minutes_per_round = 10
    rounds_needed = cherries_needed // cherries_pitted_per_round
    total_minutes = rounds_needed * minutes_per_round
    hours_needed = total_minutes / 60
    result = hours_needed
    return result

print(solution())