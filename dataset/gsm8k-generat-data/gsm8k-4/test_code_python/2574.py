def solution():
    """Yvonne swims 10 laps in 5 minutes.  Her younger sister can swim half as many laps as Yvonne in the same time frame.  Their brother Joel can swim three times the number of laps as the youngest sister.  How many laps can Joel swim?"""
    # Define Yvonne's laps and time
    yvonne_laps = 10
    yvonne_time = 5

    # Define Yvonne's sister's laps as half of Yvonne's laps
    sister_laps = yvonne_laps / 2

    # Define Joel's laps as three times Yvonne's sister's laps
    joel_laps = sister_laps * 3

    result = joel_laps
    return result

print(solution())