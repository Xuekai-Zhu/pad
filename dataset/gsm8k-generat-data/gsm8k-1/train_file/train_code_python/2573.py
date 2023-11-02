def solution():
    """Yvonne swims 10 laps in 5 minutes. Her younger sister can swim half as many laps as Yvonne in the same time frame. Their brother Joel can swim three times the number of laps as the youngest sister. How many laps can Joel swim?"""
    yvonne_laps = 10
    sister_laps = yvonne_laps / 2
    joel_laps = sister_laps * 3
    result = joel_laps
    return result

print(solution())