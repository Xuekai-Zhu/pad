def solution():
    """Mrs. Carlton gives out penalty points whenever her students misbehave. They get 5 points for interrupting, 10 points for insulting their classmates, and 25 points for throwing things. If they get 100 points, they have to go to the office. Jerry already interrupted twice and insulted his classmates 4 times. How many times can he throw things before he gets sent to the office?"""
    # Define the penalty points for each misbehavior
    interrupt_points = 5
    insult_points = 10
    throw_points = 25

    # Define the current penalty points for Jerry
    current_points = interrupt_points * 2 + insult_points * 4

    # Calculate the maximum number of times Jerry can throw things without reaching 100 points
    max_throw_times = (100 - current_points) // throw_points
    
    result = max_throw_times
    return result

print(solution())