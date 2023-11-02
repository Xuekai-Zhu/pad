def solution():
    """Yvonne swims 10 laps in 5 minutes. Her younger sister can swim half as many laps as Yvonne in the same time frame. Their brother Joel can swim three times the number of laps as the youngest sister. How many laps can Joel swim?"""
    yvonne_laps = 10
    yvonne_time = 5
    sister_laps = yvonne_laps / 2
    sister_time = yvonne_time
    joel_laps = 3 * sister_laps
    joel_time = sister_time
    result = joel_laps
    return result

print(solution())