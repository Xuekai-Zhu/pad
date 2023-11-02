def solution():
    """Mrs. Carlton gives out penalty points whenever her students misbehave. They get 5 points for interrupting, 10 points for insulting their classmates, and 25 points for throwing things. If they get 100 points, they have to go to the office. Jerry already interrupted twice and insulted his classmates 4 times. How many times can he throw things before he gets sent to the office?"""
    total_points = 0
    total_points += 5 * 2 # 2 interruptions
    total_points += 10 * 4 # 4 insults
    remaining_points = 100 - total_points # points left to reach 100
    throws_allowed = remaining_points // 25 # integer division
    result = throws_allowed
    return result

print(solution())