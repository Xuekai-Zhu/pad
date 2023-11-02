def solution():
    """Yvonne swims 10 laps in 5 minutes. Her younger sister can swim half as many laps as Yvonne in the same time frame. Their brother Joel can swim three times the number of laps as the youngest sister. How many laps can Joel swim?"""
    # Define the number of laps Yvonne can swim in 5 minutes
    yvonne_laps = 10

    # Calculate the number of laps Yvonne's sister can swim in 5 minutes
    sister_laps = yvonne_laps / 2

    # Calculate the number of laps Joel can swim in 5 minutes
    joel_laps = sister_laps * 3

    # Display the number of laps Joel can swim
    result = joel_laps
    return result

print(solution())