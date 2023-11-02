def solution():
    """Mrs. Carlton gives out penalty points whenever her students misbehave. They get 5 points for interrupting, 10 points for insulting their classmates, and 25 points for throwing things. If they get 100 points, they have to go to the office. Jerry already interrupted twice and insulted his classmates 4 times. How many times can he throw things before he gets sent to the office?"""
    # Define the points assigned to each misbehavior
    INTERRUPTION_POINTS = 5
    INSULT_POINTS = 10
    THROWING_POINTS = 25

    # Define the number of times Jerry has already misbehaved
    interruptions = 2
    insults = 4

    # Calculate the number of points Jerry has already accumulated
    points_accumulated = (interruptions * INTERRUPTION_POINTS) + (insults * INSULT_POINTS)

    # Calculate the maximum number of times Jerry can still throw things before reaching 100 points
    throwing_limit = (100 - points_accumulated) // THROWING_POINTS

    # Display the throwing limit
    result = throwing_limit
    return result

print(solution())